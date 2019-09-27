from flask import Blueprint

mn = Blueprint("main", __name__)

from webapp.main import routes
