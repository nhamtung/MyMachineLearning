from flask import send_from_directory, render_template
from app import app


@app.route('/')
@app.route('/manage')
def mainPage():
    return send_from_directory('.', 'views/main.html')


@app.route('/users')
def manageUsers():
    return send_from_directory('.', 'views/manageUser.html')


@app.route('/users/add')
def add():
    return send_from_directory('.', 'views/adduser.html')


@app.route('/books')
def manageBooks():
    return send_from_directory('.', 'views/manageBook.html')


@app.route('/books/add')
def addBooks():
    return send_from_directory('.', 'views/addBook.html')


@app.route('/recognize')
def recognizeUser():
    return send_from_directory('.', 'views/recognize.html')


@app.route('/checkin/log')
def viewLog():
    return send_from_directory('.', 'views/checkInLog.html')

@app.route('/books/<code>')
def viewBookDetail(code):
    print('book_code= '+code)
    return render_template('bookDetail.html', code=code)