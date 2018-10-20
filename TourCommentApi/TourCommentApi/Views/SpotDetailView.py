# -*- coding: utf-8 -*-
from rest_framework.views import APIView

from .CommonView import *
from ..Statics.Websites import *;
from ..Models.ConnectToDBModel import *;
from ..Models.RegionInfoModel import *;
import datetime

def get_spot_detail(request,id):
    try:
        #获取景区对象后加载数据
        #当前的景区
        curr_spot = (regioninfo.objects.get(id=str(id))).search_key;
        spots = [(regioninfo.objects.get(id = str(id))).search_key];
        #若当前景区不是千岛湖 需要加上千岛湖
        if(id != '1'):
            spots.append('千岛湖');
        if(int(datetime.datetime.now().month) < 4):
            #返回第几周
            now_date = str(datetime.datetime.now().year) + '-' + str((datetime.datetime.now().isocalendar())[1]).zfill(2);
            time = '周';
            time_search_key = 'comment_week';
        else:
            now_date = str(datetime.datetime.now().year) + '-' + (str(datetime.datetime.now().month).zfill(2));
            time = '月';
            time_search_key = 'comment_month';



        start_date = str(datetime.datetime.now().year) + '-01';
        #这里需要进行判断如果是6月前 返回周 如果是6月后 返回月 增加time字段
        now_month = str(datetime.datetime.now().year).join('-').join(str(datetime.datetime.now().month).zfill(2));
        #获取开始至结束时间段
        time_list = get_time_list(start_date,now_date,time);
        res = {};
        numAxis = [];
        scoreAxis = [];
        #获取景区数据
        comments_data = get_comment_data();
        #这里统计始终是本月
        spot_comment_data =  comments_data[
            (comments_data['search_key'] == curr_spot) & (comments_data['comment_month'] == now_month)];
        res['monthCommentNumber'] = spot_comment_data.iloc[:,0].size;
        res['monthCommentScore'] = get_score(spot_comment_data['comment_score'].mean());
        res['yearCommentNumber'] = comments_data[
            (comments_data['search_key'] == curr_spot) & (comments_data['comment_year'] == str(datetime.datetime.now().year))].iloc[:,0].size;
        #获取排名
        res['rank'] = get_rank(curr_spot);
        #返回时间区间和时间颗粒度
        res['endTime'] = time_list[-1];
        res['startTime'] = time_list[0];
        res['time'] = time;
        for j, spot in enumerate(spots):
            num_region_res = {};
            score_region_res = {};

            num_cnts = [];
            score_cnts = [];

            for k, time in enumerate(time_list):
                #获取景区数据
                comments_data = get_comment_data();
                spot_comments_data = comments_data[
                    (comments_data['search_key'] == spot) & (comments_data[time_search_key] == time)];
                num_cnts.append(spot_comments_data.iloc[:, 0].size);
                score_cnts.append(get_score((spot_comments_data['comment_score'].mean())));
            num_region_res['name'] = spot;
            num_region_res['data'] = num_cnts;
            score_region_res['name'] = spot;
            score_region_res['data'] = score_cnts;
            numAxis.append(num_region_res);
            scoreAxis.append(score_region_res);

        res['xAxis'] = time_list;
        res['numAxis'] = numAxis;
        res['scoreAxis'] = scoreAxis;
        return json_response(res);
    except Exception:
        return json_error(error_string="查询发生错误", code=11,api = "spotdetailcompared");







class SpotDetailView(APIView):

    def get(self, request,id, *args, **kwargs):
        try:

            return get_spot_detail(request,id);
        except KeyError:
            return json_error(error_string="请求错误", code=500);