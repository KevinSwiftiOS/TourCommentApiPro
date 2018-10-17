# -*- coding: utf-8 -*-
from rest_framework.views import APIView

from .CommonView import *
from ..Statics.Websites import *;
from ..Models.ＣonnectToDBModel import *;
from ..Models.RegionInfoModel import *;
import datetime

def get_spot_detail(request,id):
    #获取景区对象后加载数据
    spot = (regioninfo.objects.get(id = str(id))).search_key;
    search_keys = [(regioninfo.objects.get(id = str(id))).search_key];
    if(id != '1'):
        search_keys.append('千岛湖');

    nowMonth = str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month).zfill(2);
    startMonth = str(datetime.datetime.now().year) + '-01';
    #获取开始至结束时间段
    time_list = get_time_list(startMonth,nowMonth,'月');
    res = {};
    numAxis = [];
    scoreAxis = [];
    spot_comment_data =  comments_data[
        (comments_data['search_key'] == spot) & (comments_data['comment_month'] == nowMonth)];
    res['monthCommentNumber'] = spot_comment_data.iloc[:,0].size;
    res['monthCommentScore'] = round(spot_comment_data['comment_score'].mean(), 1);
    res['yearCommentNumber'] = comments_data[
        (comments_data['search_key'] == spot) & (comments_data['comment_year'] == str(datetime.datetime.now().year))].iloc[:,0].size;
    #获取排名
    res['rank'] = get_rank(spot);
    for j, region in enumerate(search_keys):
        num_region_res = {};
        score_region_res = {};

        num_cnts = [];
        score_cnts = [];

        for k, time in enumerate(time_list):
            jq_comment_data = comments_data[
                (comments_data['search_key'] == region) & (comments_data['comment_month'] == time)];
            num_cnts.append(jq_comment_data.iloc[:, 0].size);
            score_cnts.append(round(jq_comment_data['comment_score'].mean(),1));
        num_region_res['name'] = region;
        num_region_res['data'] = num_cnts;
        score_region_res['name'] = region;
        score_region_res['data'] = score_cnts;
        numAxis.append(num_region_res);
        scoreAxis.append(score_region_res);

    res['xAxis'] = time_list;
    res['numAxis'] = numAxis;
    res['scoreAxis'] = scoreAxis;

    #
    # jq_comment_data = comments_data[
    #     (comments_data['search_key'] == '千岛湖') & (comments_data['comment_month'] == nowMOnth)];
    # res['monthCommentNumber'] = jq_comment_data.iloc[:, 0].size;
    # res['monthCommentScore'] = round(jq_comment_data['comment_score'].mean(), 1);
    # #景区排名还未写
    # res['rank'] = '3/16';
    return json_response(res);







class SpotDetailView(APIView):

    def get(self, request,id, *args, **kwargs):
        try:

            return get_spot_detail(request,id);
        except KeyError:
            return json_error(error_string="请求错误", code=500);