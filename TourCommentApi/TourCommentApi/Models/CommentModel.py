from mongoengine import  *

# connect(db='dspider2',
#     username='lab421',
#     password='lab421_1',
#     host='120.55.59.187',
# port = 28117,
#         authentication_source='admin');
class Comments(Document):
     data_website = StringField(required=True)
     data_region = StringField(required=True)
     data_source = StringField(required=True)
     comment_user_name = StringField(required=True)
     shop_name = StringField(required=True)
     comment_content = StringField(required=True)
     comment_time = DateTimeField(required=True)
     comment_score = FloatField(required=True)
     crawl_time = DateTimeField(required=True)