# -*- coding: utf-8 -*-
from rest_framework.views import APIView

from .CommonView import *

from ..Models.ＣonnectToDBModel import *;
import datetime

def get_qdh_state(request):
    res = {};
    nowMOnth = str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month).zfill(2);

    jq_comment_data = comments_data[
        (comments_data['search_key'] == '千岛湖') & (comments_data['comment_month'] == nowMOnth)];
    res['monthCommentNumber'] = jq_comment_data.iloc[:, 0].size;
    res['monthCommentScore'] = round(jq_comment_data['comment_score'].mean(), 1);
    #景区排名还未写
    res['rank'] = get_rank('千岛湖');
    return json_response(res);







class QdhStateView(APIView):

    def get(self, request, *args, **kwargs):
        try:

            return get_qdh_state(request);
        except KeyError:
            return json_error(error_string="请求错误", code=500);
