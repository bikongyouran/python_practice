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

if __name__ == '__main__':
    app.run(debug=True)

