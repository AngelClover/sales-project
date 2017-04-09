from flask import jsonify, request, current_app, url_for, g
from flask_login import login_required
from . import api
#from ..models import User, AnonymousUser
from .. import db
from .errors import bad_request, unauthorized, forbidden
from .authentication import auth
from .decorators import permission_required, admin_required
import re
import os

UPLOAD_DIR ="../uploadfiles"

def secure_filename(file_name):
    secure_name = re.sub('[" \-~\|\-/]', '_', file_name)
    return secure_name   

def target_filename(name):
    return os.path.join(UPLOAD_DIR, name)

def get_right_filename(name):
    name = name.decode('string-escape')
    name = name.decode('utf-8')
    name = secure_filename(name)
    if os.path.exists(target_filename(name)):
        a = os.path.splitext(name)
        index = 0
        while True:
            name = a[0] + "_" + str(index) + a[1]
            if os.path.exists(target_filename(name)) == False:
                break;
            index += 1
    return name

    

@api.route('/upload', methods=['POST'])
#@auth.login_required
def upload_file():
#file.save()
#upload_json = request.get_json()
#print upload_json
#    if upload_json is None:
#        return bad_request('content error')
    filename = "bad filename"
    try:
#print request
#print request.__dict__
        file = request.files['file']
        filename = get_right_filename(file.filename)
        target = target_filename(filename)
        print 'save file -> ', target
        file.save(target)

    except Exception as e:
        return bad_request('parse error')

    return jsonify({
            'error' : 0,
            'msg' : 'xx',
            'data' : {'filename': filename},
            })
