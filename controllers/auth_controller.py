from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from sqlalchemy import select
from models.db import db
from flask_login import login_user, login_required, logout_user
from models import User, Role
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__, 
                    template_folder="./views/", 
                    static_folder='./static/', 
                    root_path="./")

@auth.route("/")
@auth.route("/login")
def login():
    return render_template("auth/login.html")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@auth.route('/login_post', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()
    
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))
    
    login_user(user, remember=remember)
    return redirect(url_for('admin.admin_index'))

@auth.route('/signup')
def signup():
    return render_template("auth/signup.html")

@auth.route('/signup_post', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    username = request.form.get("username", None)
    email = request.form.get("email", None)
    password = request.form.get("password", None)
    
    try:
        new_user = User(username=username, email=email, password=generate_password_hash(password, method='sha256'),role='client')
        new_user.roles.append(Role(name='client'))

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.login'))
    except:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))