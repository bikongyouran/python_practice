from flask import Blueprint

myApp = Blueprint("homePage", __name__, template_folder='templates')
graphApp = Blueprint("graph", __name__, template_folder='templates')

from . import homePage,graph