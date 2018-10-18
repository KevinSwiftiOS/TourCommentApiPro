# -*- coding: utf-8 -*-
from pymongo import *
from pandas import *
import datetime
import math

from ..Statics.Regions import *
from ..Statics.Websites import *
#client = MongoClient("mongodb://lab421:lab421_1@127.0.0.1:28117/")
client = MongoClient('localhost',27017);

database = client['dspider2']
comments_tb = database.comments;

comments_data = DataFrame(list(comments_tb.find()));
#转换年份的 返回2018
def convert_year(comment_time):
    return comment_time[0:4];

#转化季度的 返回2018-03
def convert_season(comment_time):
    times = comment_time.split('-');
    year = (times[0]);
    month = int(times[1]);
    if month % 3 == 0:
        return year + '-' + (str(int(3 / 3))).zfill(2);
    else:
        return  year + '-' + (str(math.floor(month / 3) + 1)).zfill(2);

#转化月份的 返回2018-03
def convert_month(comment_time):
    times = comment_time.split('-');
    year = times[0];
    month = times[1];
    return year + '-' +  month;



#转化周的 返回2018-03 和返回第几天 2018-36
def convert_week(comment_time):
    t = comment_time.split('-');
    return t[0] + '-' +  str((datetime.date(int(t[0]), int(t[1]), int(t[2])).isocalendar())[1]).zfill(2);
def convert_day(comment_time):
    t = comment_time.split('-');
    return t[0] + '-' + ((str(datetime.date(int(t[0]), int(t[1]), int(t[2])).isocalendar())[2]).zfill(2));

def convert_data_region_search_key(data_region):
    for i, search_key in enumerate(search_keys):
        if search_key in data_region:
            return search_key;
    return "";
# 转换商品店铺名的 方便查询
def convert_shop_name_search_key(shop_name):
    for i,shop_search_key in enumerate(shop_name_search_keys):
        if shop_search_key in shop_name:
            return shop_search_key;
    return "";



#取出关于景点的评论
comments_data = comments_data[comments_data['data_source'] == '景点'];

#转换年份
comments_data['comment_year'] = comments_data['comment_time'].apply(convert_year);
#转换季度
comments_data['comment_season'] = comments_data['comment_time'].apply(convert_season);
#转换月份
comments_data['comment_month'] = comments_data['comment_time'].apply(convert_month);
#转换周
comments_data['comment_week']= comments_data['comment_time'].apply(convert_week);
#转换天
comments_data['comment_day']= comments_data['comment_time'].apply(convert_day);



#转换商品店铺关键字
comments_data['search_key'] = comments_data['data_region'].apply(convert_data_region_search_key);
comments_data['shop_name_search_key'] = comments_data['shop_name'].apply(convert_shop_name_search_key);
now_month = str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month).zfill(2);
#景区排名数组

#统计该月的评分 随后排序
def get_valued_score(score):
    if score is np.nan:
        return 0;
    else:
        return round(score,1);
def get_spot_ranks(search_key):
    dic = {};
    spot_comment_data = comments_data[
        (comments_data['search_key'] == str(search_key)) & (comments_data['comment_month'] == str(now_month))];

    dic['search_key'] = search_key;
    dic['comment_num'] = get_valued_score(spot_comment_data.iloc[:,0].size);
    return dic;


def get_zhejiang_spot_ranks(search_key):
    dic = {};
    spot_comment_data = comments_data[
        (comments_data['search_key'] == str(search_key)) & (comments_data['comment_month'] == str(now_month))];

    dic['search_key'] = search_key;
    dic['comment_num'] = get_valued_score(spot_comment_data.iloc[:, 0].size);
    return dic;
#获取景区排名
spot_ranks = [get_spot_ranks(search_key) for search_key in search_keys];
inner_spot_ranks = [get_zhejiang_spot_ranks(search_key) for search_key in zhe_jiang_search_keys];



spot_ranks = sorted(spot_ranks, key=lambda x: x['comment_num'],reverse=True);

inner_spot_ranks = sorted(inner_spot_ranks, key=lambda x: x['comment_num'],reverse=True);
spot_ranks_dic = {};
for i,dic in enumerate(inner_spot_ranks):
    spot_ranks_dic[dic['search_key']] = str(i + 1)  + '/16';
for i,dic in enumerate(spot_ranks):
    if dic['search_key'] =='黄山' or dic['search_key'] == '三清山':
        if(i <= 15):
          spot_ranks_dic[dic['search_key']] = '相当于省内第' + str(i + 1) + '名';
        else:
            spot_ranks_dic[dic['search_key']] = '相当于省内第16名';


region_website_spot_dic = {};

for i,region in enumerate(search_keys):
    #暂时是景点的数据取出 后期会有酒店 餐饮的评论等
    for j,website in enumerate(websites):
        region_website_spot_dic[str(region) + '_' + str(website) + ("_景点")] = comments_data[
        (comments_data['search_key'] == str(region)) & (comments_data['data_website'] == str(website))

        ];





#






