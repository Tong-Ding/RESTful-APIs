from sqlalchemy import or_
from app.libs.redprint import Redprint
from app.models.book import Book
from app.validators.forms import BookSearchForm
from flask import jsonify, request

api = Redprint('book')


@api.route('/search')
def search():
    form = BookSearchForm().validate_for_api()    # 创建Form对象时自动获取request信息
    q = '%' + form.q.data + '%'  # sql模糊搜索要前后加%
    # book = Book()
    # 元类 ORM
    books = Book.query.filter(or_(Book.title.like(q), Book.publisher.like(q))).all()  # or_模糊搜索
    books = [book.hide('summary') for book in books]
    return jsonify(books)


@api.route('/<isbn>/detail')
def detail(isbn):
    book = Book.query.filter_by(isbn=isbn).first_or_404()
    return jsonify(book)


@api.route('/get')
def get_book():
    return "get book"


@api.route('/post', methods=['POST'])
def post_book():
    a = request.json
    return a
