# -*- coding: utf-8 -*-
from rest_framework.views import APIView

from .CommonView import *

from ..Models.ＣonnectToDBModel import *
from ..Models.RegionInfoModel import *




def hasResult(region):

        data = {};
        data['id'] = region.id;
        data['name'] = region.name;
        data['address'] = region.address;
        data['lng'] = region.lng;
        data['lat'] = region.lat;
        #进行搜索
        jq_comments = comments_data[(comments_data['search_key'] == str(region.search_key))]



        data['commentNumber'] =   jq_comments.iloc[:, 0].size;
        data['commentScore'] = round(jq_comments['comment_score'].mean(), 1);
        # data['score'] = comments.count();
        return data;
def get_spot_list(request):
   #进行解码token
    # username = decodeToken(request);
    # print(username);
    res = {};
    list = [];


    try:
        list = [hasResult(region) for region in regioninfo.objects];
       # 返回所有的文档对象列表
        res['list'] = list;
        return json_response(res);
    except Exception:
        return json_error(error_string='查询发生错误',code = 11);



class SpotListView(APIView):

    def get(self, request, *args, **kwargs):
        try:

            return get_spot_list(request);
        except KeyError:
            return json_error(error_string="请求错误", code=500);
