# myapp/__init__.py 

from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
import os
from os import environ, path 
from flask_migrate import Migrate
from flask_login import LoginManager
from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import Accomplishments
from myapp.accomplishments.forms import AccomplishmentForm

accomplishments = Blueprint('accomplishments', __name__)


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

############################
###### DATABASE SETUP ######
############################


# set up connection to db
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost:5432/accomplishments"
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.init_app(app)
Migrate(app, db)


#############################

############ LOGIN CONFIGS ##############

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'





# Registering Blueprints - 

from myapp.core.views import core 
app.register_blueprint(core)

#linking the 404 and 403 error pages into the app 
from myapp.error_pages.handlers import error_pages
app.register_blueprint(error_pages)


#linking users views Blueprint
from myapp.users.views import users
app.register_blueprint(users)

# Linking and registering accomplishments views Blueprint
from myapp.accomplishments.views import accomplishments
app.register_blueprint(accomplishments)