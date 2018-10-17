# -*- coding: utf-8 -*-
from pymongo import *
from pandas import *
import datetime
from ..Statics.Regions import *
client = MongoClient("mongodb://lab421:lab421_1@10.1.17.25:27517/")


database = client['dspider2']
comments_tb = database.comment;
shops_tb = database.shop;

shops_data = DataFrame(list(shops_tb.find()))
comments_data = DataFrame(list(comments_tb.find()))

def convert_year(str):
    return str[0:4];



comments_data['comment_year'] = comments_data['comment_time'].apply(convert_year);
#shop_name的书写
# comments_data['shop_name_search_key'] = comments_data['shop_name'].apply(convert_shop_name_search_key);
nowMonth = str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month).zfill(2);
total_search_keys = [];

for i,search_key in enumerate(search_keys):
    dic = {};
    spot_comment_data  =  comments_data[
        (comments_data['search_key'] == str(search_key)) & (comments_data['comment_month'] == str(nowMonth))];

    dic['search_key'] = search_key;
    dic['comment_score']  = round(spot_comment_data['comment_score'].mean(),1);
    total_search_keys.append(dic);

total_search_keys = sorted(total_search_keys, key=lambda x: x['comment_score'],reverse=True);




