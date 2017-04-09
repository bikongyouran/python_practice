from flask import render_template,session,redirect,url_for,flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from . import myApp
# from ..models import User
# from .. import db
#
# @myApp.route('/user/<name>')
# def user(name):
#     testUser = User(name, name + '@test.com')
#     db.session.add(testUser)
#     db.session.commit()
#     return 'hello, %s!' % name

@myApp.route('/', methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('.index'))
    return render_template('user.html', form=form, name=session.get('name'))

@myApp.route('/d3', methods=['GET','POST'])
def d3_test():
    return render_template('d4.html')

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')
