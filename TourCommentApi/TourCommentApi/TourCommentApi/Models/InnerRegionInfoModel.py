# -*- coding: utf-8 -*-
from mongoengine import  *


class innerregioninfo(Document):
     _id = BinaryField(required=True)
     id = StringField(required=True)
     address = StringField(required=True)
     name = StringField(required=True)
     lng = FloatField(required=True)
     lat = FloatField(required=True)
     search_key = StringField(required=True)
