from flask import render_template, flash, redirect, url_for
from app import app


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


@app.route('/login', methods=['GET','POST'])
def Login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login Requested for user {}, Remember_me={}'.format(form.username.data,form.remember_me.data))
        print('Login Requested for user {}'.format(form.username.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In',form=form)


@app.route('/user')
def userProfile():
    return ("potato")