from functools import wraps
from flask import g
from .errors import forbidden
from ..models import Permission, AnonymousUser


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not g.current_user.can(permission):
                return forbidden('Insufficient permissions')
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def admin_required():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not g.current_user.can(Permission.MODULE_PERMISSION_DICT['administer']):
                return forbidden('Not admin')
            return f(*args, **kwargs)
        return decorated_function
    return decorator
