from flask import Flask
from views import myApp

app = Flask(__name__)
app.register_blueprint(myApp)
