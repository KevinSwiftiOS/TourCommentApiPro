# -*- coding: utf-8 -*-
from rest_framework.views import APIView
import datetime
from ..Models.ConnectToDBModel import *;
from .CommonView import *


def get_qdh_state(request):
    try:
        res = {};
        now_month = str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month).zfill(2);
        #获取景区数据
        comments_data = get_comment_data();
        qdh_comment_data = comments_data[
            (comments_data['search_key'] == '千岛湖') & (comments_data['comment_month'] == now_month)];
        res['monthCommentNumber'] = qdh_comment_data.iloc[:, 0].size;
        res['monthCommentScore'] = get_score(qdh_comment_data['comment_score'].mean());
        #景区排名还未写
        res['rank'] = get_rank('千岛湖');
        return json_response(res);
    except Exception:
        return json_error(error_string="查询发生错误", code=12,api = "qdhstate");


class QdhStateView(APIView):

    def get(self, request, *args, **kwargs):
        try:

            return get_qdh_state(request);
        except KeyError:
            return json_error(error_string="请求错误", code=500);
