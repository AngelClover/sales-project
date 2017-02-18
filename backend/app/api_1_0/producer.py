#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import jsonify, request, g, url_for, current_app
from .. import db
from ..models import Equipment, Producer, Permission
from . import api
from decorators import permission_required
from errors import bad_request

@api.route('/producer/headers', methods=['GET', 'POST'])
def get_producer_headers():
    return jsonify({
            'error' : 0,
            'msg' : '',
            'data' : Producer.get_headers()
            })


