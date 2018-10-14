from rest_framework.views import APIView

from .CommonView import *

from ..Models.CommentModel import comment
from ..Models.RegionInfoModel import *


def get_jingqu_list(request):
   #进行解码token
    # username = decodeToken(request);
    # print(username);
    res = {};
    list = [];
    try:
        for region in regioninfo.objects:
            data = {};
            data['id'] = region.id;
            data['name'] = region.name;
            data['address'] = region.address;
            data['lng'] = region.lng;
            data['lat'] = region.lat;
            #进行搜索
            comments = comment.objects(data_region__contains = region.search_key);
            data['commentNumber'] = comments.count();
            data['score'] = round(comments.average('comment_score'),1);
            list.append(data);
       # 返回所有的文档对象列表
        res['list'] = list;
        return json_response(res);
    except Exception:
        return json_error(error_string='查询发生错误',code = 11);



class JingquListView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            return get_jingqu_list(request);
        except KeyError:
            return json_error(error_string="请求错误", code=500);
