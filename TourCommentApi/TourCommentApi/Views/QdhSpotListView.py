from rest_framework.views import APIView
import datetime

from ..Models.InnerRegionInfoModel import innerregioninfo
from ..Models.ConnectToDBModel import *
from .CommonView import *
#获取一个景区的 随后进行迭代
def get_one_qdh_spot(inner_region,qdh_comment_data):

    data = {};
    data['id'] = inner_region.id;
    data['name'] = inner_region.name;
    data['address'] = inner_region.address;
    data['lng'] = inner_region.lng;
    data['lat'] = inner_region.lat;
    # 进行搜索

    qdh_one_spot_comment_data = qdh_comment_data[qdh_comment_data['shop_name_search_key'] == str(inner_region.search_key)];


    data['commentNumber'] = qdh_one_spot_comment_data.iloc[:, 0].size;
    data['commentScore'] = get_score(qdh_one_spot_comment_data['comment_score'].mean());
    return data;

def get_qdh_spot_list(request):
    # 进行解码token
    # username = decodeToken(request);
    # print(username);
    try:
        res = {};

        #增加本月评分和评论数量
        now_month = str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month).zfill(2);
        #获取数据
        comments_data = get_comment_data();
        #统计本月的 如果是总共的？
        qdh_comment_data = comments_data[
            (comments_data['search_key'] == '千岛湖')];


        list = [get_one_qdh_spot(inner_region,qdh_comment_data) for inner_region in innerregioninfo.objects];
            # 返回所有的文档对象列表

        res['list'] = list;
        return json_response(res);
    except Exception:
        return json_error(error_string='查询发生错误', code=12,api = 'qdhspotlist');

class QdhSpotListView(APIView):

    def get(self, request, *args, **kwargs):
        try:

            return get_qdh_spot_list(request);
        except KeyError:
            return json_error(error_string="请求错误", code=500);
