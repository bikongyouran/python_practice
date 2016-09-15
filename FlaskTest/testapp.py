from flask import Flask,render_template,session,redirect,url_for,flash
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
#prevent csrf. this config should be written in config file.
app.config['SECRET_KEY'] = 'hard to guess string'
Bootstrap(app)

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('user.html', form=form, name=session.get('name'))

@app.route('/user/<name>')
def user(name):
    return 'hello, %s!' % name

@app.route('/users')
def user2():
    return render_template('user.html', name = 'aaa')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)

