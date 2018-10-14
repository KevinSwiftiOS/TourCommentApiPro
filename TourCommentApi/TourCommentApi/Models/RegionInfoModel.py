from mongoengine import  *


class regioninfo(Document):
     _id = BinaryField(required=True)
     id = StringField(required=True)
     address = StringField(required=True)
     name = StringField(required=True)
     lng = FloatField(required=True)
     lat = FloatField(required=True)
     search_key = StringField(required=True)
