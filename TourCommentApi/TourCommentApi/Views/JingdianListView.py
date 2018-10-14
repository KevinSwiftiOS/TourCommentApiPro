from rest_framework.views import APIView

from .CommonView import *

from ..Models.CommentModel import comment
from ..Models.InnerRegionInfoModel import innerregioninfo


def get_jingdian_list(request,id):
    # 进行解码token
    # username = decodeToken(request);
    # print(username);
    res = {};
    list = [];
    allComments = comment.object();
    try:
        for region in innerregioninfo.objects:
            data = {};
            data['id'] = region.id;
            data['name'] = region.name;
            data['address'] = region.address;
            data['lng'] = region.lng;
            data['lat'] = region.lat;
            # 进行搜索
            comments = allComments(shop_name__contains=region.search_key);
            data['commentNumber'] = comments.count();
            data['score'] = round(comments.average('comment_score'), 1);
            list.append(data);
        # 返回所有的文档对象列表
        res['list'] = list;
        return json_response(res);
    except Exception:
        return json_error(error_string='查询发生错误', code=11);

class JingdianListView(APIView):

    def get(self, request,id, *args, **kwargs):
        try:
            print(id);
            return get_jingdian_list(request,id);
        except KeyError:
            return json_error(error_string="请求错误", code=500);
