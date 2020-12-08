import numpy as np
import dlib
import math
from PIL import Image
import cv2
import db_service
from app import db
import os
import utils

EMBED_SIZE = 128
EMBED_DISTANCE_THRESH = 0.3

REAL_FACE = 0
UNREAL_FACE = 1

SHARPNESS_THRESHOLD = 60
FACE_DATA_DIR = 'data/face_data'

(IMAGE_WIDTH, IMAGE_HEIGHT) = (640, 480)
VALID_FACE_HEIGHT_RATIO = 0.4

face_detector = dlib.get_frontal_face_detector()
pose_predictor = dlib.shape_predictor(
    "models/shape_predictor_68_face_landmarks.dat")
face_encoder = dlib.face_recognition_model_v1(
    'models/dlib_face_recognition_resnet_model_v1.dat')
#anti_face_profing_model = AntiProofing.load_anti_proofing_model()


def getRectArea(rect):
    w = rect.right() - rect.left()
    h = rect.bottom() - rect.top()
    return w * h


def getFaceLocation(img_array):
    locations = face_detector(img_array)
    if len(locations) == 1:
        # locations = sorted(locations, key=getRectArea, reverse=True)
        return locations[0]
    elif len(locations) > 1:
        locations = sorted(locations, key=getRectArea, reverse=True)
        return locations[0]
    return None


def isRealFace(full_img_array, face_loc):
    img_array = full_img_array[face_loc.top(
    ):face_loc.bottom(), face_loc.left():face_loc.right()]
    # Scale image to AntiProofing.IMAGE_SIZE
    image = Image.fromarray(img_array, mode='RGB')

    # calculate sharpness value
    sharpness = cv2.Laplacian(np.array(image), cv2.CV_64F).var()
    print('face\' sharpness = ', sharpness)
    if sharpness < SHARPNESS_THRESHOLD:
        return False

    return True


def getFaceEncode(img_array, face_location=None):
    if face_location is None:
        face_location = getFaceLocation(img_array)

    if face_location is not None:
        face_landmark = pose_predictor(img_array, face_location)
        return (utils.landmark_to_np(face_landmark),np.array(face_encoder.compute_face_descriptor(img_array, face_landmark), dtype=np.float32))
    return None


def findClosestUser(img_array, face_location):
    (_,face_encode) = getFaceEncode(img_array, face_location)

    if face_encode is not None:
        face_encode = np.array([face_encode])
        users = db_service.getAllUsers()
        if users is not None:
            distances = []

            for user in users:
                data_file = os.path.join(FACE_DATA_DIR, '{}_{}/face_encode.np'.format(user.staff_code, user.fullname))
                data = np.fromfile(data_file, dtype=np.float32)
                data = data.reshape(-1, EMBED_SIZE)
                distance2 = np.min(np.sum((data - face_encode)**2, axis=1))
                distance = math.sqrt(distance2)
                distances.append(distance)

            if len(distances) > 0:
                imin = np.argmin(distances)
                dist = distances[imin]
                print(dist)
                if dist <= EMBED_DISTANCE_THRESH:
                    print('{}-user: {}_{}'.format(dist,user.staff_code, user.fullname))
                    return users[imin]

    return None

def isValidFace(top, left, size):
    if top < 0 or left < 0 or top + size > IMAGE_HEIGHT or left + size > IMAGE_WIDTH:
        return False
    return size >= VALID_FACE_HEIGHT_RATIO * IMAGE_HEIGHT
