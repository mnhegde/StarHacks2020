from flask import Flask, render_template, session, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime
from hashpassword import makePasswordHash, checkPasswordHash


app = Flask(__name__)

app.config['SECRET_KEY'] = 'hello'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'


db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    farmname = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(50), unique=True, nullable=False)
    farmtype = db.Column(db.String(50))
    about = db.Column(db.String(1000))
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default=datetime.now)


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.now)
    description = db.Column(db.String(1000))


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        username = data['username']
        password = data['password']
        flag = False
        
        farms = db.session.query(User).all()
        for farm in farms: 
            if farm.username == username: 
                flag = True
                if checkPasswordHash(password, farm.password):
                    return 'logged in'
                else:
                    flash('The user doesn\'t exist or the password provided was incorrect', 'error')
                    return redirect('/login')

        if not flag:
            flash('The user doesn\'t exist or the password provided was incorrect', 'error')
            return redirect('/login')  

        return 'good'
    else:
        return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        data = request.form
        username = request.form['username']
        email = request.form['email']
        firstname = request.form['firstName']
        lastname = request.form['lastName']
        password = request.form['password']
        confirmPassword = request.form['confirmPassword']

        if password == confirmPassword:
            farms = db.session.query(User).all()
            for farm in farms:
                if farm.username == username:
                    flash('This username already exists', 'error')
                    return redirect('/signup')
            password = makePasswordHash(confirmPassword)
            farm = User[username, password, firstname, lastname, email]
            db.session.commit(farm)
            db.session.commit()
            return 'signed up and logged in'
        else:
            flash('Passwords didn\'t match!', 'error')
            return redirect('/signup')  
    else:
        return render_template('signup.html') 

@app.route('/',  methods = ['GET','POST'])
@app.route('/home',  methods = ['GET','POST'])
def index():
    return render_template('home.html')


@app.route('/about',  methods = ['GET','POST'])
def home():
    return render_template('about.html')

@app.route('/farms', methods = ['GET','POST'])
def farms():
    farms = db.session.query(User).all()
    return render_template('farms.html', farms=farms)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)