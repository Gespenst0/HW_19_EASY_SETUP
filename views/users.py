import hashlib

from flask import request
from flask_restx import Resource, Namespace
from models import User
from setup_db import db

user_ns = Namespace('users')


@user_ns.route('/')
class UserView(Resource):
    def post(self):
        req_json = request.json
        if "password" not in req_json:
            return("You have not entered your password!")
        if "role" not in req_json:
            req_json["role"] = "user"
        ent = User(**req_json)
        ent.create_pass(req_json)
        db.session.add(ent)
        db.session.commit()
        return "", 201
