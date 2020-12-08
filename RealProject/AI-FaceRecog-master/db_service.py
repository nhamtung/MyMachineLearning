from app import db
import time
import numpy as np


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    staff_code = db.Column(db.String(20), unique=True, nullable=False)
    fullname = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.fullname


class CheckIn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    staff_code = db.Column(db.String(80), nullable=False)
    book_code = db.Column(db.String(80))
    checkin_time = db.Column(db.DateTime, nullable=False)
    # is_checkin_book = db.Column(db.Boolean, nullable = True)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String, unique = True,nullable=False)
    name = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(300), nullable=True)


def getUserByCode(staff_code):
    return User.query.filter_by(staff_code=staff_code).first()


def getAllUsers():
    return User.query.all()

def getUserList():
    users = getAllUsers()
    return [{'staff_code': user.staff_code,'fullname': user.fullname} for user in users]


def addUser(staff_code, fullname):
    user = User(fullname=fullname, staff_code=staff_code)
    db.session.add(user)
    db.session.commit()
    return user


def deleteUser(staff_code):
    user = getUserByCode(staff_code)
    if user:
        db.session.delete(user)
        db.session.commit()
    return user


def addCheckIn(staff_code,book_code, checkin_time):
    checkin = CheckIn(staff_code=staff_code, checkin_time=checkin_time,book_code=book_code)
    # if book_code != "":
    #     checkin.is_checkin_book = CheckIn.query.filter_by(staff_code = staff_code, book_code = book_code).count() % 2 ==0
    db.session.add(checkin)
    db.session.commit()
    return checkin

def isCheckinBook(staff_code, book_code):
    checkinList = CheckIn.query.filter_by(staff_code = staff_code, book_code = book_code)
    if not checkinList:
        return True
    else:
        return checkinList.count() % 2 !=0
    return False

def getLastCheckInTimeByUser(staff_code):
    checkin = CheckIn.query.filter_by(staff_code=staff_code).order_by(CheckIn.checkin_time.desc()).first()
    return checkin.checkin_time if checkin else None


def getCheckInHistory():
    checkIns = CheckIn.query \
        .join(User, CheckIn.staff_code == User.staff_code) \
        .outerjoin(Book, CheckIn.book_code == Book.code) \
        .order_by(CheckIn.checkin_time.desc()) \
        .add_columns(User.fullname, CheckIn.checkin_time, Book.name.label('book_name')) \
        .all()

    # checkIns = CheckIn.query \
    #     .join(User, CheckIn.staff_code == User.staff_code) \
    #     .add_columns(User.fullname, CheckIn.checkin_time) \
    #     .all()
    return [{'fullname': checkIn.fullname, 'time': checkIn.checkin_time.strftime('%H:%M:%S %d/%m/%Y'), 'bookname':checkIn.book_name}
               for checkIn in checkIns]


def getBookDetail(code):
    book = Book.query.filter_by(code=code).first()
    if book:
        return {
                'name':book.name,
                'author': book.author,
                'description': book.description}
def getBook(code):
    book = Book.query.filter_by(code=code).first()
    if book:
        return book

def getListBook():
    books = Book.query.all()
    return [{'code': book.code, 'name':book.name, 'author':book.author, 'description':book.description} for book in books]

def addBook(name, author, description, code=None):
    book = Book(name=name, author=author, description=description)
    if code is None:
        book.code = str(int(round(time.time() * 1000)))
    else:
        book.code = code
    db.session.add(book)
    db.session.commit()
    return book


def deleteBook(code):
    book = getBook(code)
    if book:
        db.session.delete(book)
        db.session.commit()
