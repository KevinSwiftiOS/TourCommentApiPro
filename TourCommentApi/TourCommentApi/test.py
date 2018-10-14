from mongoengine import  *
import datetime
import re
connect(db='dspider2',
    username='lab421',
    password='lab421_1',
    host='120.55.59.187',
port = 28117,
        authentication_source='admin');


class regioninfo(Document):
    _id = BinaryField(required=True)
    id = StringField(required=True)
    address = StringField(required=True)
    name = StringField(required=True)
    lng = FloatField(required=True)
    lat = FloatField(required=True)
    search_key = StringField(required=True)


if __name__ == '__main__':
   # regionInfos = regioninfo.objects(name__contains = '千岛湖');
   # print(regionInfos.get().name);
   # print(regionInfos.count());
   #进行时间的分割
   startTime = '2017-06';
   endTime = '2018-10';


   start_year = startTime.split('-')[0];
   start_date = startTime.split('-')[1];
   end_year = endTime.split('-')[0];
   end_date = endTime.split('-')[1];
   while start_year < end_year:


   # for region in regioninfo.objects:
   #     print(region.name)