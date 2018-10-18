# -*- coding: utf-8 -*-
from rest_framework.views import APIView
import datetime
from ..Statics.Websites import *
from ..Models.RegionInfoModel import regioninfo
from ..Models.ConnectToDBModel import *
from .CommonView import *
def get_data(comments_data,isNum):

    if(isNum == "1"):
        return comments_data.iloc[:,0].size;
    else:
        return get_score(comments_data['comment_score'].mean());


#获取一个景区上的
def get_website_data(website, spot, time_search_key,compared_time,is_num):


    # 一个景区在平台上的评论
    spot_website_comments_data = region_website_spot_dic[spot + ('_') + (website) + ("_景点")];

    cnts = get_data(spot_website_comments_data[
                (spot_website_comments_data[time_search_key] == compared_time)],is_num);


    return cnts;

#获取一个网站上的
def get_spot_data(spot,time_search_key,compared_time,is_num):

    spot_res = {};
    # 时间颗粒度的获取

    # 在时间颗粒度中进行遍历
    #字段含义 网站 景区 时间搜索颗粒度 时间区间 统计评分或者数量
    spot_res['data'] = [get_website_data(website, spot, time_search_key,compared_time,is_num) for website in websites];

    spot_res['name'] = spot;
    return spot_res;


#获取景区比较
def post_spot_detail_compard(request):

    #post中拿到景区列表 和开始结束时间
    body = json.loads(request.body);
    id = (body['id']);

    #从数据库中抽取
    spots = [(regioninfo.objects.get(id = str(id))).search_key];

    if(id != '1'):
        spots.append('千岛湖');
    #景区的比较时间
    compared_time = (body['compared_time']);
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

        #外面一层平台遍历 里面一层景区遍历

    res = {};

    #字段含义 网站 时间搜索颗粒度 时间跨度 景区搜索关键字 统计评分还是数量
    res['yAxis'] = [get_spot_data(spot,time_search_keys[time],compared_time,is_num) for spot in spots];
    res['xAxis'] = websites;

    return json_response(res);











#千岛湖与其余景区同时段评论数量比较
class SpotDetailComparedView(APIView):

    def post(self, request, *args, **kwargs):
        try:

            return post_spot_detail_compard(request);
        except KeyError:
            return json_error(error_string="请求错误", code=500);
