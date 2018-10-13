from mongoengine import  *

connect(db='dspider2',
    username='lab421',
    password='lab421_1',
    host='120.55.59.187',
port = 28117,
        authentication_source='admin');
class User(Document):
     username = StringField(required=True)
     password = StringField(required=True)
     _id = BinaryField(required=True)