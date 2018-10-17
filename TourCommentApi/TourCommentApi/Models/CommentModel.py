# -*- coding: utf-8 -*-
from mongoengine import  *


class comment(Document):
     data_website = StringField(required=True)
     data_region = StringField(required=True)
     data_source = StringField(required=True)
     comment_user_name = StringField(required=True)
     shop_name = StringField(required=True)
     comment_content = StringField(required=True)
     comment_time = StringField(required=True)
     comment_score = FloatField(required=True)
     comment_month = StringField(required=True)
     comment_season = StringField(required=True)
     crawl_time = DateTimeField(required=True)

