from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from PIL import Image
from datetime import datetime
import numpy as np
import dlib
import io
import os
import shutil
import json
import math
# import AntiProofing
import base64
import cv2
import face_utils
import time
import glob
import cv2
from app import db, app
from db_service import User, addCheckIn, getLastCheckInTimeByUser, getCheckInHistory
import db_service
import qrcode_recog

db.create_all()
FACE_DATA_DIR = "data/face_data"
QR_DATA_DIR = "data/qr_data"
CHECKIN_DATA_DIR = "data/checkin_data"

SERVER_SUCCESS = 0
SERVER_FAKE_IMAGE = 1
SERVER_USER_NOT_EXIST = 2
SERVER_INVALID_FACE = 3
SERVER_NO_QR_CODE = 4
SERVER_USER_EXISTED = 5

CHECKIN_TIMEOUT = 10


def drawFaceLandmark(img_array, face_landmark):
    face_shape = face_landmark[:17]
    left_eye = face_landmark[36:42]
    left_eyebrown = face_landmark[17:22]
    right_eye = face_landmark[42:48]
    right_eyebrown = face_landmark[22:27]
    nose_dosum = face_landmark[27:31]
    nose_tip = face_landmark[31:36]
    mouth = face_landmark[48:]

    cv2.polylines(img_array, [face_shape], False, (0, 255, 0))
    cv2.polylines(img_array, [left_eye], False, (0, 255, 0))
    cv2.polylines(img_array, [left_eyebrown], False, (0, 255, 0))
    cv2.polylines(img_array, [right_eye], False, (0, 255, 0))
    cv2.polylines(img_array, [right_eyebrown], False, (0, 255, 0))
    cv2.polylines(img_array, [nose_dosum], False, (0, 255, 0))
    cv2.polylines(img_array, [nose_tip], False, (0, 255, 0))
    cv2.polylines(img_array, [mouth], False, (0, 255, 0))


def addNewUser(staff_code, fullname, img_array):
    face_data = face_utils.getFaceEncode(img_array)
    data_dir_path = os.path.join(
        FACE_DATA_DIR, '{}_{}'.format(staff_code, fullname))

    if face_data is not None:
        (face_landmark, face_encode) = face_data
        face_encode = np.array([face_encode])
        user = db_service.getUserByCode(staff_code)

        if not user:
            user = db_service.addUser(staff_code, fullname)

        if user:
            if not os.path.exists(data_dir_path):
                os.mkdir(data_dir_path)

            face_encode_path = os.path.join(data_dir_path, 'face_encode.np')
            face_image_path = os.path.join(data_dir_path, '{}.jpg'.format(
                len(glob.glob(data_dir_path+'/*.jpg'))+1))

            if os.path.exists(face_encode_path):
                face_encode_data = np.fromfile(
                    face_encode_path, dtype=np.float32)
                face_encode_data = face_encode_data.reshape(
                    -1, face_utils.EMBED_SIZE)
                face_encode_data = np.concatenate(
                    (face_encode_data, face_encode), axis=0)
            else:
                face_encode_data = face_encode
            face_encode_data.tofile(face_encode_path)
            # save image with facelandmark to file
            drawFaceLandmark(img_array, face_landmark)
            cv2.imwrite(face_image_path, cv2.cvtColor(
                img_array, cv2.COLOR_RGB2BGR))
            print('added user: ', staff_code, '-', fullname,
                  ' ', os.path.basename(face_image_path))


def getBookFromImage(image_data):
    qrData = qrcode_recog.readQRCode(image_data)
    print('qrData: ',qrData)
    if qrData is not None:
        (_, _, _, _, qrCode) = qrData
        book = db_service.getBook(qrCode)
        print ("code: ",qrCode,"- book: ",book)
        if book:
            return book
    return None


# @app.route('/qr/<path:code>')
# def getQRImage():
#     fileName = code + '.jpg'
#     return send_from_directory(directory=QR_DATA_DIR, filename=fileName)


@app.route('/qr/book_code')
def getBookCodeAPI():
    code = str(int(round(time.time() * 1000)))
    return jsonify({'code': code})


@app.route('/user/get_users')
def getUserDataAPI():
    users = db_service.getUserList()
    return jsonify(users)


@app.route('/get_books')
def getListBookAPI():
    return jsonify(db_service.getListBook())


@app.route('/books/book_detail', methods=['POST'])
def getBookDetailAPI():
    code = request.json['code']
    book = db_service.getBookDetail(code)
    return jsonify(book)


@app.route('/delete_book', methods=['POST'])
def deleteBookAPI():
    book_code = request.json['book_code']
    db_service.deleteBook(book_code)
    return jsonify('OK')


@app.route('/qr/save_book', methods=['POST'])
def saveBookAPI():
    code = request.json['book_code']
    name = request.json['book_name']
    author = request.json['book_author']
    description = request.json['book_description']
    db_service.addBook(name=name,
                       author=author,
                       description=description,
                       code=code)
    return jsonify('OK')


@app.route('/get_checkin_history')
def getCheckInHistoryAPI():
    checkIns = getCheckInHistory()
    return jsonify(checkIns)


@app.route('/add_user_image', methods=['POST'])
def addUserImageAPI():
    image_data = request.json['image_data']
    staff_code = str(request.json['staff_code'])
    fullname = str(request.json['fullname'])
    image_data = image_data[23:]
    bytes = base64.b64decode(image_data)
    img_array = np.array(Image.open(io.BytesIO(bytes)))

    face_location = face_utils.getFaceLocation(img_array)
    if face_location is None or not face_utils.isValidFace(face_location.top(), face_location.left(), face_location.right() - face_location.left()) or not face_utils.isRealFace(img_array, face_location):
        print('add_user_image {}-{}: INVALID_FACE'.format(staff_code,fullname))
        return jsonify({'code': SERVER_INVALID_FACE})
    addNewUser(staff_code, fullname, img_array)
    print('add_user_image {}-{}: SUCCESS'.format(staff_code,fullname))
    return jsonify({'code': SERVER_SUCCESS})


@app.route('/user/check_user', methods=['POST'])
def checkUserAPI():
    staff_code = str(request.json['staff_code'])
    user = db_service.getUserByCode(staff_code)

    if not user:
        return jsonify({'code': SERVER_USER_NOT_EXIST})
    else:
        return jsonify({'code': SERVER_USER_EXISTED})


@app.route('/delete_user', methods=["POST"])
def deleteUserAPI():
    staff_code = str(request.json['staff_code'])
    user = db_service.deleteUser(staff_code)
    fullname = user.fullname
    face_data_dir = os.path.join(FACE_DATA_DIR, '{}_{}'.format(staff_code, fullname))
    if os.path.exists(face_data_dir):
        shutil.rmtree(face_data_dir, ignore_errors=True)
    return jsonify('OK')


@app.route('/recognize', methods=['POST'])
def recognizeAPI():
    image_data = request.json['image_data']
    image_data = image_data[23:]
    # print(image_data)

    bytes = base64.b64decode(image_data)
    img = Image.open(io.BytesIO(bytes))
    img_array = np.array(img)

    face_location = face_utils.getFaceLocation(img_array)
    if face_location is not None and face_utils.isValidFace(face_location.top(), face_location.left(), face_location.right() - face_location.left()):
        # if face_utils.isRealFace(img_array, face_location):
        if True:
            user = face_utils.findClosestUser(img_array, face_location)
            if not user:
                print('User is not existed')
                return jsonify({'code': SERVER_USER_NOT_EXIST,
                                'face_top': face_location.top(),
                                'face_left': face_location.left(),
                                'face_size': face_location.right() - face_location.left()})
           
            lastCheckInTime = getLastCheckInTimeByUser(user.staff_code)
            currentTime = datetime.now()
            if not lastCheckInTime or (currentTime - lastCheckInTime).seconds >= CHECKIN_TIMEOUT:
                book = getBookFromImage(img_array)
                if book is None:
                    addCheckIn(
                            staff_code=user.staff_code,
                            book_code="",
                            checkin_time=currentTime)
                    print('No QR code')
                    return jsonify({
                                'code': SERVER_NO_QR_CODE,
                                'face_top': face_location.top(),
                                'face_left': face_location.left(),
                                'face_size': face_location.right() - face_location.left(),
                                'staff_code': user.staff_code,
                                'fullname': user.fullname,
                                'checkin_time': currentTime.strftime("%d/%m/%Y  %H:%M:%S")
                                })

                addCheckIn(
                            staff_code=user.staff_code,
                            book_code=book.code,
                            checkin_time=currentTime)
                return jsonify({'code': SERVER_SUCCESS,
                                'is_checkin': db_service.isCheckinBook(user.staff_code, book.code),
                                'staff_code': user.staff_code,
                                'fullname': user.fullname,
                                'face_top': face_location.top(),
                                'face_left': face_location.left(),
                                'face_size': face_location.right() - face_location.left(),
                                'book_name': book.name,
                                'book_author':book.author,
                                'checkin_time': currentTime.strftime("%d/%m/%Y  %H:%M:%S")
                                })
        else:
            return jsonify({'code': SERVER_FAKE_IMAGE})
    print('No face')
    return jsonify({'code': SERVER_INVALID_FACE})


if __name__ == '__main__':
    if not os.path.exists(FACE_DATA_DIR):
        os.mkdir(FACE_DATA_DIR)

    if not os.path.exists(QR_DATA_DIR):
        os.mkdir(QR_DATA_DIR)

    if not os.path.exists(CHECKIN_DATA_DIR):
        os.mkdir(CHECKIN_DATA_DIR)

    app.run(host="0.0.0.0", port=5000, threaded=False,ssl_context=('cert.pem', 'key.pem'))
    # app.run(host="0.0.0.0", port=5000, threaded=False)
