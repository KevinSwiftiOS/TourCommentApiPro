from rest_framework.views import APIView

from .CommonView import *

from ..Models.CommentModel import *
from ..Models.RegionInfoModel import *
from django.db import connection
from django.core.cache import cache
from pymongo import *;
from pandas import *;
from threading import Timer
# 设置一个 key
key = 'article'
# 判断 key 是否存在 cache 中， 存在则在 cache 中取， 不存在则查询数据库




# client = MongoClient("mongodb://lab421:lab421_1@10.1.17.25:27517/")
#
#
# database = client['dspider2']
# comments_tb = database.comment;
# shops_tb = database.shop;
#
# shops_data = DataFrame(list(shops_tb.find()))
# comments_data = DataFrame(list(comments_tb.find()))
comments_data = DataFrame();
def hasResult(region):

        data = {};
        data['id'] = region.id;
        data['name'] = region.name;
        data['address'] = region.address;
        data['lng'] = region.lng;
        data['lat'] = region.lat;
        #进行搜索
        filter1 = comments_data[(comments_data['comment_season'] == '2018-01')]



        data['commentNumber'] =   filter1.iloc[:, 0].size;
        # data['score'] = comments.count();
        return data;
def get_jingqu_list(request):
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



class JingquListView(APIView):

    def get(self, request, *args, **kwargs):
        try:

            return get_jingqu_list(request);
        except KeyError:
            return json_error(error_string="请求错误", code=500);
