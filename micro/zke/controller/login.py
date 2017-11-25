# -*- coding:utf-8 -*-
import hashlib

import tornado.web
from model.Assignment import *
from logic.access import *
from base import BaseHandler
from logic.access import *



@needcheck()
class LoginHandler(BaseHandler):
    def get(self):
        self.render("login.html")
    def post(self):
        name = self.get_argument('name')
        password = self.get_argument('password')
        kwargs['password']  =  hashlib.md5(password).hexdigest()
        user = User.objects(name=name,password=password).first()
        if user:
            self.set_secure_cookie("uid",str(user.id))
            status,msg = True,'successs'
        else:
            status,msg = False,'fail'
        self.write(dict(status=status,msg=msg))