from flask import Flask,render_template,session,redirect,url_for,flash
from flask_bootstrap import Bootstrap
from . import myApp

myApp.config['SECRET_KEY'] = 'hard to guess string'
Bootstrap(myApp)

@myApp.route('/user/<name>')
def user(name):
    return 'hello, %s!' % name

@myApp.route('/users')
def user2():
    return render_template('user.html', name = 'aaa')

@myApp.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@myApp.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500