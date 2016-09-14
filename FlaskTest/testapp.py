from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def hello():
    return 'hello world!'

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

