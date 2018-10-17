# -*- coding: utf-8 -*-
from rest_framework.views import APIView

from .CommonView import *

from ..Models.CommentModel import comment
from ..Models.RegionInfoModel import regioninfo
from ..Models.ＣonnectToDBModel import *
import datetime

def get_spot_compard(request):

    #post中拿到景区列表 和开始结束时间
    body = json.loads(request.body);
    search_keys = body['spots'];
    print(111);
    print(search_keys);
    startTime = body['startTime'];
    endTime = body['endTime'];
    websites =body['websites'];
    #是评论数量还是评分
    type = body['type'];
    #获取时间颗粒度
    time = body['time'];
        #加上默认的千岛湖
    search_keys.append('千岛湖');
    time_list = get_time_list(startTime,endTime,type);
        #外面一层平台遍历 里面一层景区遍历

    res = {};
    list = [];
    for i,website in enumerate(websites):
    # for i, website in enumerate(websites):
        websiteRes = {};
        # 时间颗粒度的获取

        # 在时间颗粒度中进行遍历
        yAxis = [];
        for j, region in enumerate(search_keys):
            regionRes = {};
            cnts = [];

            for k, time in enumerate(time_list):

                if (type == '月'):
                    jq_comment_data = comments_data[
                        (comments_data['search_key'] == region) & (comments_data['comment_month'] == time) & (comments_data['data_website'] == website)];
                elif (type == '季度'):
                    jq_comment_data = comments_data[
                        (comments_data['search_key'] == '千岛湖') & (comments_data['comment_season'] == time) & (comments_data['data_website'] == website)];

                cnts.append(jq_comment_data.iloc[:, 0].size);

            regionRes['name'] = region;
            regionRes['data'] = cnts;
            yAxis.append(regionRes);
        websiteRes['website'] = website;
        websiteRes['xAxis'] = time_list;
        websiteRes['yAxis'] = yAxis;

        list.append(websiteRes);

    res['list'] = list;
    return json_response(res);











#千岛湖与其余景区同时段评论数量比较
class SpotComparedView(APIView):

    def post(self, request, *args, **kwargs):
        try:

            return get_spot_compard(request);
        except KeyError:
            return json_error(error_string="请求错误", code=500);
