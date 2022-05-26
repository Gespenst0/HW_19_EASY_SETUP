import jwt
from flask import request, abort
from config import Config


def auth_required(func):
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)

        return func(*args, **kwargs)

    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        JWT_SECRET = Config.JWT_SECRET
        JWT_ALGO = Config.JWT_ALGO

        if "Authorization" not in request.headers:
            abort(401)

        data = request.headers("Authorization")
        token = data.split("Bearer ")[-1]
        role = None

        try:
            user = jwt.decode(token, JWT_SECRET, algoritmhs=[JWT_ALGO])
            role = user.get("role", "user")
        except Exception as e:
            print("JWT Decode Exprion", e)

        if role != "admin":
            abort(403)

        return func(*args, **kwargs)

    return wrapper
