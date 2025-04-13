import os
from datetime import datetime

from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

from forms import RegisterForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['WTF_CSRF_SECRET_KEY'] = 'secret'
app.config['SECRET_KEY'] = 'secret'

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'db_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now())
    update_time = db.Column(db.DateTime, nullable=False, default=datetime.now())


class UserAddress(db.Model):
    __tablename__ = 'db_user_address'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('db_user.id'))
    address = db.Column(db.String(80), nullable=False)
    user = db.relationship('User', backref=db.backref('address', lazy=True))
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now())
    update_time = db.Column(db.DateTime, nullable=False, default=datetime.now())


@app.route('/')
def index():
    return "Hello"


@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():

        user = User(username=register_form.username.data, password=register_form.password.data)
        db.session.add(user)
        db.session.commit()
    else:
        print(register_form.errors)
    return render_template('register_form.html', register_form=register_form)


@app.route('/user/<int:page>')
def list_user(page):
    user_page_data = User.query.paginate(page=page)
    return render_template('list_user.html', user_page_data=user_page_data)


@app.route('/img/upload', methods=['GET', 'POST'])
def image_upload():
    if request.method == 'POST':
        files = request.files
        file = files.get('img', None)
        if file is not None:
            file_name = secure_filename(file.filename)
            file.save(os.path.join(r"D:\pythob_web\tmp", file_name))
            return redirect(url_for('image_upload'))
    return render_template('image_upload.html')


def init_database():
    with app.app_context():
        db.drop_all()
        db.create_all()
        # add_user()


def add_user():
    for i in range(1000):
        user = User(username=f'user{i}', password='123456')
        db.session.add(user)

    db.session.commit()


if __name__ == '__main__':
    init_database()
    app.run(debug=True)
