from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
Bootstrap(app)

# config for db
# Here need to install mysql-python first. specially, use 'conda install mysql-python' instead of 'pip install mysql-python'.
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost/myFlaskDB'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

'''Attention: should put the blueprint import at the end, so that not introduce the circular import issue!!!'''
from views import myApp,graphApp
app.register_blueprint(myApp)
app.register_blueprint(graphApp)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500




