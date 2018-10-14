from rest_framework.views import APIView

from .CommonView import *

from ..Models.CommentModel import comment
from ..Models.RegionInfoModel import regioninfo

import datetime

def get_jingqu_detail(request,id):
    data_region = regioninfo.objects(id = id);
    search_key = data_region.get().search_key;


    res = {};
    list = [];
    #今年 金月的评论总分和评论数量 排名还未做

    this_year_comments = comment.objects(data_region__contains = search_key,comment_time__contains = str(datetime.datetime.now().year));
    last_year_comments = comment.objects(data_region__contains=search_key,
                                         comment_time__contains=str(datetime.datetime.now().year - 1));

    #判断景区评论数量是否上升和评论总数
    res['thisYearCommentNumber'] = this_year_comments.count();
    res['thisYearCommentNumberIsRise'] =  1 if (this_year_comments.count() > last_year_comments.count()) else 0;
    #这个月
    this_year_month = str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month).zfill(2);
    #s上个月
    last_year_month = "";
    if(datetime.datetime.now().month == 1):
        last_year_month += str(datetime.datetime.now().year - 1) + '-12';
    else:
        last_year_month += str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month - 1).zfill(2);
    this_year_month_comments = comment.objects(data_region__contains = search_key,
                                               comment_time__contains = this_year_month);
    last_year_month_comments = comment.objects(data_region__contains = search_key,
                                               comment_time__contains = last_year_month);
    res['thisMonthCommentScore'] = round(this_year_month_comments.average('comment_score'),1);
    res['thisMonthCommentScoreIsRising'] = 1 if (this_year_month_comments.average('comment_score') > last_year_month_comments.average('comment_score')) else 0;
    res['thisMonthCommentNumber'] = this_year_month_comments.count();
    res['thisMonthCommentNumberIsRising'] = 1 if (
                this_year_month_comments.count() > last_year_month_comments.count()) else 0;


    return json_response(res);





class JingquDetailView(APIView):

    def get(self, request,id, *args, **kwargs):
        try:
            print(id);
            return get_jingqu_detail(request,id);
        except KeyError:
            return json_error(error_string="请求错误", code=500);
