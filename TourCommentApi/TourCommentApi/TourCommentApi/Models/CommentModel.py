<<<<<<< HEAD:TourCommentApi/TourCommentApi/TourCommentApi/Models/CommentModel.py
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

=======
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

>>>>>>> 7e6f8e4230555896acacc7a72ae975759fb7d685:TourCommentApi/TourCommentApi/Models/CommentModel.py
