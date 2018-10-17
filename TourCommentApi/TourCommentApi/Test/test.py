# -*- coding: utf-8 -*-
from mongoengine import  *
import datetime
import re
# from .Models.RegionInfoModel import *;
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

def return2Value(i):
    return 1,i + 1;
if __name__ == '__main__':
    x = 4
    a = [1,2,3,4];

    b = ([return2Value(i) for i in a]);
    print(type(b));
    time = '2018-09-03';
    t = time.split('-');
    print((datetime.date(int(t[0]),int(t[1]),int(t[2])).isocalendar())[1]);
    print(11111);
    print(a[-1]);
    # dict = [
    #     {'id': '4', 'name': 'b'},
    #     {'id': '6', 'name': 'c'},
    #     {'id': '3', 'name': 'a'},
    #     {'id': '1', 'name': 'g'},
    #     {'id': '8', 'name': 'f'}
    # ]
    # dict = sorted(dict, key=lambda x: x['id'],reverse=True)
    # for(i,j) in enumerate(dict):
    #     print(i,j);
    #     print(j['name']);
    # regionInfos = regioninfo.objects.get(id = '1');
   # print(regionInfos.search_key);
   # time = '2018-09-10';
   # print(time[0:4]);
   # print(regionInfos.get().name);
   # print(regionInfos.count());
   #进行时间的分割
   # startTime = '2018-01';
   # endTime = '2018-03';
   # for  i in range(0,5):
   #     print(i);
   #
   #
   # start_year = int(startTime.split('-')[0]);
   # start_date = int(startTime.split('-')[1]);
   # end_year = int(endTime.split('-')[0]);
   # end_date = int(endTime.split('-')[1]);
   # time_list = [];
   # #开始结束年份不同 需将月份加上
   # if(start_year < end_year):
   #   first = True;
   #   for year in range(start_year,end_year + 1):
   #       if (year != end_year):
   #         if(first):
   #           first = False;
   #           for month in range(start_date,13):
   #               time_list.append(str(year) + '-' + str(month).zfill(2));
   #         else:
   #           for month in range(1, 13):
   #               time_list.append(str(year) + '-' + str(month).zfill(2));
   #       else:
   #           for month in range(1,end_date + 1):
   #               time_list.append(str(year) + '-' + str(month).zfill(2));
   # #开始结束年份相同 只需遍历日期即可
   # else:
   #  for month in range(start_date,end_date + 1):
   #      time_list.append(str(start_year) + '-' + str(month).zfill(2));
   #
   #
   #
   #
   # search_keys = ['千岛湖','西湖'];
   # websites = ['携程','去哪儿'];
   # type = '月';
   # # 在时间颗粒度中进行遍历
   # res = {};
   # list = [];
   # for i,website in enumerate(websites):
   #     websiteRes = {};
   #     # 时间颗粒度的获取
   #
   #     # 在时间颗粒度中进行遍历
   #     yAxis = [];
   #     for j, region in enumerate(search_keys):
   #         regionRes = {};
   #         cnts = [];
   #
   #         for k, time in enumerate(time_list):
   #             print(region)
   #             print(time)
   #             print(website)
   #             if (type == '月'):
   #                 comments = comment.objects(data_website=website, data_region__contains=region, comment_month=time);
   #             elif (type == '季度'):
   #                 comments = comment.objects(data_website=website, data_region__contains=region, comment_season=time);
   #
   #             cnts.append(comments.count());
   #             print(cnts);
   #         regionRes['name'] = region;
   #         regionRes['data'] = cnts;
   #         yAxis.append(regionRes);
   #     websiteRes['website'] = website;
   #     websiteRes['xAxis'] = time_list;
   #     websiteRes['yAxis'] = yAxis;
   #
   #     list.append(websiteRes);
   #     print(list);
#    sql = {
#        'data_website':'去哪儿',
#        'comment_month':'2018-09',
#    }
#    sql1 = {
#        'data_website':'携程'
#    }
#    # comments = comment.objects(Q(__raw__=sql) | Q(__raw__ = sql1))
#    # for comment in comments:
#    #     print(comment.data_website);
#    # print(comments.count())
#    # region_comment = comments(data_region__contains = '千岛湖')
#    # print(region_comment.count())
#
# def aaaa(s):
#         print(1);
#         return s + 1;
# def set1():
#     print(222);
#
#     a = [aaaa(i) for i in range(0,5)]
#     print(a);
#
# set1();

   # for region in regioninfo.objects:
   #     print(region.name)
