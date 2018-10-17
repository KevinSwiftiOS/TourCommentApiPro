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
def get_region_data(website,region,time_search_key,time_list,isNum):

    region_res = {};
    # 一个景区在平台上的评论
    spot_website_comments_data = region_website_spot_dic[region.join('_').join(website).join("_景点")];
    cnts = [get_data(spot_website_comments_data[
                (spot_website_comments_data[time_search_key] == time)],isNum) for time in
            time_list];

    region_res['name'] = region;
    region_res['data'] = cnts;
    return region_res;

#获取一个网站上的
def get_website_data(website,time_search_key, time_list,spot_search_keys,isNum):

    website_res = {};
    # 时间颗粒度的获取

    # 在时间颗粒度中进行遍历
    #字段含义 网站 景区 时间搜索颗粒度 时间区间 统计评分或者数量
    yAxis = [get_region_data(website, region, time_search_key, time_list,isNum) for region in spot_search_keys];
    website_res['website'] = website;
    website_res['xAxis'] = time_list;
    website_res['yAxis'] = yAxis;
    return website_res;


#获取景区比较
def post_spot_compard(request):

    #post中拿到景区列表 和开始结束时间
    body = json.loads(request.body);
    spot_search_keys = (body['spots']);


    startTime = body['startTime'];

    endTime = body['endTime'];

    websites = (body['websites']);

    #是评论数量还是评分
    isNum = body['type'];

    #获取时间颗粒度
    time = body['time'];
    #
        #加上默认的千岛湖


    time_list = get_time_list(startTime,endTime,time);
        #外面一层平台遍历 里面一层景区遍历

    res = {};
    list = [];
    if(time == '月'):
        #时间颗粒度搜索关键字
        time_search_key = 'comment_month';
    elif (time == '季度'):
        time_search_key = 'comment_season';
    #字段含义 网站 时间搜索颗粒度 时间跨度 景区搜索关键字 统计评分还是数量
    list = [get_website_data(website,time_search_key,time_list,spot_search_keys,isNum) for website in websites];

    res['list'] = list;
    return json_response(res);











#千岛湖与其余景区同时段评论数量比较
class SpotComparedView(APIView):

    def post(self, request, *args, **kwargs):
        try:

            return post_spot_compard(request);
        except KeyError:
            return json_error(error_string="请求错误", code=500);
