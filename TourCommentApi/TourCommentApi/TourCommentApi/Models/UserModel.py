# -*- coding: utf-8 -*-
from mongoengine import  *

class user(Document):
     username = StringField(required=True)
     password = StringField(required=True)
     _id = BinaryField(required=True)