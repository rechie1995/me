# coding: utf-8
from flask import render_template, session, redirect, url_for, flash, request, Response, jsonify, g
from datetime import datetime
from flask_login import login_required, login_user, logout_user, current_user
from flask_nav.elements import *

from . import main
from .forms import NameForm, LoginForm, RegistrationForm, SettingsForm, ChoicesForm
from .. import db, nav, login_manager
from ..models import User
from ..camera import VideoCamera

nav.register_element('top', Navbar(u'Webcam', View(u'主页','main.index'),
                                                View(u'设置','main.settings'), 
                                                View(u'登出','main.logout')
                                                ))
@main.before_request
def before_request():
    g.user = current_user

@main.route('/', methods = ['Get','Post'])
def first():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('main.index'))
    else:
        return redirect(url_for('main.login'))

@main.route('/index', methods = ['Get', 'Post'])
@login_required
def index():
    form = ChoicesForm()
    if form.validate_on_submit():
 #       user = User.query.filter_by(username=form.name.data).first()
 #       if user is None:
 #           session['known'] = False
 #       else:
 #           session['known'] = True
 #       session['name'] = form.name.data
 #       form.name.data = ''
        return redirect(url_for('main.video_feed'))
    return render_template("index.html", 
            form = form, 
            name = session.get('name'),)
 #           known = session.get('known', False))

@main.route('/user/<name>')
def user(name):
    return render_template("user.html",name = name)

@main.route('/settings')
@login_required
def settings():
    form = SettingsForm()
    return render_template("settings.html", form = form, name = session.get('name'))


@main.route('/login', methods = ['Get', 'Post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(url_for('main.index'))
        flash('Invalid username or password.')
    return render_template('login.html', title = 'Sign In', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    session['name'] = ''
    flash('You have been logged out.')
    return redirect(url_for('main.login'))

@main.route('/register', methods=['Get', 'Post'])
def register():
    form =  RegistrationForm()
    if form.validate_on_submit():
        user = User(username = form.username.data,
                    password = form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You can now login.')
        return redirect(url_for('main.login'))
    return render_template('register.html', title = 'Register', form=form)
    
@main.route('/webcam', methods=['Get', 'Post'])
def webcam():
    return render_template('webcam.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
                b'Content_Type:image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@main.route('/video_feed')
@login_required
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')