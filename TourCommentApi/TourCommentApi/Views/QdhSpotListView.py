from rest_framework.views import APIView

from .CommonView import *

from ..Models.CommentModel import comment
from ..Models.InnerRegionInfoModel import innerregioninfo
from ..Models.ＣonnectToDBModel import *
import datetime
def get_qdh_spot_list(request):
    # 进行解码token
    # username = decodeToken(request);
    # print(username);
    res = {};
    list = [];
    #增加本月评分和评论数量
    nowMOnth = str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month).zfill(2);

    jq_comment_data = comments_data[
        (comments_data['search_key'] == '千岛湖') & (comments_data['comment_month'] == nowMOnth)];

    allComments = comment.objects();
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
            data['commentScore'] = round(comments.average('comment_score'), 1);
            list.append(data);
        # 返回所有的文档对象列表
        res['monthCommentNumber'] = jq_comment_data.iloc[:, 0].size;
        res['monthCommentScore'] = round(jq_comment_data['comment_score'].mean(), 1);
        res['list'] = list;
        return json_response(res);
    except Exception:
        return json_error(error_string='查询发生错误', code=11);

class QdhSpotListView(APIView):

    def get(self, request, *args, **kwargs):
        try:

            return get_qdh_spot_list(request);
        except KeyError:
            return json_error(error_string="请求错误", code=500);
