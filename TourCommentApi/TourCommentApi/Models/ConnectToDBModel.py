# -*- coding: utf-8 -*-
from pymongo import *
from pandas import *
import datetime
import math

from ..Statics.Regions import *
from ..Statics.Websites import *
client = MongoClient("mongodb://lab421:lab421_1@120.55.59.187:28117/")


database = client['dspider2']
comments_tb = database.comment;
shops_tb = database.shop;

shops_data = DataFrame(list(shops_tb.find()));
comments_data = DataFrame(list(comments_tb.find()));
#转换年份的 返回2018
def convert_year(_str):
    return _str[0:4];

#转化季度的 返回2018-03
def convert_season(_str):
    times = _str.split('-');
    year = (times[0]);
    month = int(times[1]);
    if month % 3 == 0:
        return year.join('-').join(str(month / 3));
    else:
        return  year.join('-').join(str(math.floor(month / 3) + 1));

#转化月份的 返回2018-03
def convert_month(_str):
    times = _str.split('-');
    year = times[0];
    month = times[1];
    return year.join('-').join(month);



#转化周的 返回2018-03
def convert_week(_str):
    t = _str.split('-');
    return t[0].join('-').join((str(datetime.date(int(t[0]), int(t[1]), int(t[2])).isocalendar())[1]));



# 转换商品店铺名的 方便查询
def convert_shop_name_search_key(str):
    for i,shop_search_key in enumerate(shop_name_search_keys):
        if shop_search_key in str:
            return shop_search_key;
    return "";



#取出关于景点的评论
comments_data = comments_data[comments_data['data_source'] == '景点'];

#转换年份
comments_data['comment_year'] = comments_data['comment_time'].apply(convert_year);
#转换季度
comments_data['comment_season'] = comments_data['comment_time'].apply(convert_year);
#转换月份
comments_data['comment_month'] = comments_data['comment_time'].apply(convert_year);
#转换周
comments_data['comment_week'] = comments_data['comment_time'].apply(convert_year);

#转换商品店铺关键字
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
    dic['comment_score'] = get_valued_score(spot_comment_data['comment_score'].mean());
    return dic;
#获取景区排名
spot_ranks = [get_spot_ranks(search_key) for search_key in search_keys];
spot_ranks = sorted(spot_ranks, key=lambda x: x['comment_score'],reverse=True);
region_website_spot_dic = {};
for i,region in enumerate(search_keys):
    #暂时是景点的数据取出 后期会有酒店 餐饮的评论等
    for j,website in enumerate(websites):
        region_website_spot_dic[region.join('_').join(website).join("_景点")] = comments_data[
        (comments_data['search_key'] == str(region)) & (comments_data['data_website'] == str(website))
        &(comments_data['data_source'] == '景点')
        ];





#






