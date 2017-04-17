from flask import Blueprint

test = Blueprint('test', __name__)
auth = Blueprint('auth', __name__)

import testAPI
import authAPI