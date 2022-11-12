from functools import wraps

from flask import jsonify
from flask_jwt_extended import get_jwt, verify_jwt_in_request
from flask_smorest import abort


def admin_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["is_admin"] is True:
                return fn(*args, **kwargs)
            else:
                abort(403, message="You are not authorized.")

        return decorator

    return wrapper
