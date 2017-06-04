from flask import jsonify, request, current_app, url_for, g
from flask_login import login_required
from . import api
#from ..models import User, AnonymousUser
from .. import db
from .errors import bad_request, unauthorized, forbidden
from .authentication import auth
from .decorators import permission_required, admin_required
from ..models import UploadFile
import re
import os
import random
import datetime

UPLOAD_DIR ="../uploadfiles"

def secure_filename(file_name):
    secure_name = re.sub('[" \-~\|\-/]', '_', file_name)
    return secure_name   

def target_filename(name):
    return os.path.join(UPLOAD_DIR, name)

def get_random_filename(name):
    return name
    ret = ""
    for i in range(10):
        ret += chr(ord('a') + int(random.random() * 26))
    return ret

def get_right_filename(name):
#print name
#name = name.decode('string-escape')
#   print name
#name = name.decode('utf-8')
#name = name.decode('')
#   print name
    name = secure_filename(name)
#   print name
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
@auth.login_required
def upload_file():
#file.save()
#upload_json = request.get_json()
#print upload_json
#    if upload_json is None:
#        return bad_request('content error')
    filename = "bad filename"
    dataContent = ""
    try:
#print request
#print request.__dict__
        file = request.files['file']
        print file.filename
        storeName = get_random_filename(file.filename)
        filename = get_right_filename(storeName)
        print filename
        target = target_filename(filename)
        print target
#TODO: bug that may get 0 for userid when use token
        userid = int(request.form.get('userid')) if request.form.get('userid') is not None else None
        if userid is None:
            userid = g.current_user.id
        type = request.form.get('type') if request.form.get('type') is not None else None
        print 'save file -> ', target, 'userid:', userid, 'type:', type
        file.save(target)
        today = datetime.datetime.today()
        uf = UploadFile(userid, filename, file.filename, today, type)
        try:
            db.session.add(uf)
            db.session.commit()
        except Exception as e:
            print e
            db.session.rollback()
            return bad_request('session error')
        dataContent = uf.to_json()
    except Exception as e:
        print e
        return bad_request('parse error')

    return jsonify({
            'error' : 0,
            'msg' : 'file upload success',
            'data' : dataContent,
            })

@api.route('/upload', methods=['GET', 'POST'])
def get_file_list():
    userid = int(request.args.get('userid')) if request.args.get('userid') is not None else None
    print 'userid:', userid
    files = []
    if userid is None or userid == 1:
        files = UploadFile.query.all()
    else:
        files = UploadFile.query.filter_by(userid=userid).all()
    return jsonify({
            'error' : 0,
            'msg' : '',
            'data' : {
            'headers': UploadFile.get_ordered_headers(),
            'files': [f.to_json() for f in files]
            }
            })


@api.route('/upload/<int:id>', methods=['GET', 'POST'])
def get_file(id):
    f = UploadFile.query.get_or_404(id)
    return jsonify({
            'error' : 0,
            'msg' : '',
            'data' : f.to_json()
            })

@api.route('/upload/<int:id>', methods=['DELETE'])
def delete_file(id):
    f = UploadFile.query.get_or_404(id)
    try:
        name = f.target_filename()
        print "userid:", g.current_user.id, "delete file ----->", name
        os.remove(name)
        db.session.delete(f)
        db.session.commit()
    except Exception, e:
        print e
        return jsonify({
                'error' : 1,
                'msg' : e,
                'data' : {}
                })

    return jsonify({
            'error' : 0,
            'msg' : 'delete file successful',
            'data' : {}
            })
