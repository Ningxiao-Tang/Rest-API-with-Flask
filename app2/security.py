from werkzeug.security import safe_str_cmp
from user import User

def authenticate(username, password):
    u = User.find_by_username(username)
    if u and safe_str_cmp(u.password, password):
        return u

def identity(payload):
    user_id = payload['identity']
    return User.find_by_id.get(user_id)