from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from werkzeug.security import check_password_hash

app = Flask(__name__)
CORS(app, resources={"*": {"origins": "*"}})
app.config.from_object('config')
jwt = JWTManager(app)
db  = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

import Messages
from app.components import fieldsFormatter

from app.models.rolesTable import Role
from app.models.usersTable import User
from app.models.controllersTable import Controller
from app.models.actionsTable import Action
from app.models.resourcesTable import Resource
from app.models.privilegesTable import Privilege
from app.models.servidorTable import Servidor

from app.validators.formValidator import FormValidator
from app.validators.authValidator import AuthValidator
from app.validators.userValidator import UserValidator
from app.validators.servidorValidator import ServidorValidator

from app.controllers import usersController
from app.controllers import authController
from app.controllers import servidorController