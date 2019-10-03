from flask import render_template, flash, redirect, url_for, request
from app import app
from flask_login import current_user , login_user, logout_user , login_required
from app.models import User
from werkzeug.urls import url_parse

from app.form import LoginForm


@app.route('/')
@app.route('/index')
def index():
   
    user = {'username': 'Arran'}
    posts = [
        {
            'author': {'username':'John'},
            'body': 'What a Post'
        },
        {
            'author': {'username': 'Tyler'},
            'body' : 'This website is growing!'
        }
    ]
    print("index for : " + user['username'])
    return render_template('index.html', title='Home',user=user, posts=posts)


@app.route('/login', methods=['GET' , 'POST'])
def Login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("invaild username or password.")
            return redirect(url_for('Login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page= url_for('userProfile')

        flash('Login Requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        print('Login Requested for user {}'.format(form.username.data))
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/user')
@login_required
def userProfile():
    print (current_user.username)
    return render_template ('Profile.html', title='{} Profile page'.format(current_user.username))



@app.route('/logout')
def Logout():
    logout_user()
    return redirect(url_for('index'))