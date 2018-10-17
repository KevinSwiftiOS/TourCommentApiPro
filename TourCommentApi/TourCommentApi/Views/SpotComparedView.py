# -*- coding: utf-8 -*-
from rest_framework.views import APIView
import datetime

from ..Models.RegionInfoModel import regioninfo
from ..Models.ConnectToDBModel import *
from .CommonView import *
def get_data(comments_data,isNum):

    if(isNum == "1"):
        return comments_data.iloc[:,0].size;
    else:
        return get_score(comments_data['comment_score'].mean());


#获取一个景区上的
def get_region_data(website,spot,time_search_key,time_list,is_num):

    region_res = {};
    # 一个景区在平台上的评论
    spot_website_comments_data = region_website_spot_dic[spot.join('_').join(website).join("_景点")];
    cnts = [get_data(spot_website_comments_data[
                (spot_website_comments_data[time_search_key] == time)],is_num) for time in
            time_list];

    region_res['name'] = spot;
    region_res['data'] = cnts;
    return region_res;

#获取一个网站上的
def get_website_data(website,time_search_key, time_list,spots,is_num):

    website_res = {};
    # 时间颗粒度的获取

    # 在时间颗粒度中进行遍历
    #字段含义 网站 景区 时间搜索颗粒度 时间区间 统计评分或者数量
    yAxis = [get_region_data(website, spot, time_search_key, time_list,is_num) for spot in spots];
    website_res['website'] = website;
    website_res['xAxis'] = time_list;
    website_res['yAxis'] = yAxis;
    return website_res;


#获取景区比较
def post_spot_compard(request):

    #post中拿到景区列表 和开始结束时间
    body = json.loads(request.body);
    spots = (body['spots']);


    start_time = body['startTime'];

    end_time = body['endTime'];

    websites = (body['websites']);

    #是评论数量还是评分
    is_num = body['type'];

    #获取时间颗粒度
    time = body['time'];
    #
        #加上默认的千岛湖
    time_search_keys = {
        '年':'comment_year',
        '季度':'comment_season',
        '月':'comment_month',
        '周':'comment_week'
    };

    time_list = get_time_list(start_time,end_time,time);
        #外面一层平台遍历 里面一层景区遍历

    res = {};

    #字段含义 网站 时间搜索颗粒度 时间跨度 景区搜索关键字 统计评分还是数量
    list = [get_website_data(website,time_search_keys[time],time_list,spots,is_num) for website in websites];

    res['list'] = list;
    return json_response(res);











#千岛湖与其余景区同时段评论数量比较
class SpotComparedView(APIView):

    def post(self, request, *args, **kwargs):
        try:

            return post_spot_compard(request);
        except KeyError:
            return json_error(error_string="请求错误", code=500);
