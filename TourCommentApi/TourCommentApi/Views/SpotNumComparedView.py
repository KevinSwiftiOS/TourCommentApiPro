from rest_framework.views import APIView

from .CommonView import *

from ..Models.CommentModel import comment
from ..Models.RegionInfoModel import regioninfo

import datetime

def get_spot_num_compard(request):
    #post中拿到景区列表 和开始结束时间
        search_keys = eval((request.POST.getlist('spots'))[0]);
        startTime = request.POST['startTime'];
        endTime = request.POST['endTime'];
        websites = eval((request.POST.getlist('websites'))[0]);
        type = request.POST['type'];
        print(search_keys);
        #加上默认的千岛湖
        search_keys.append('千岛湖');
        time_list = get_time_list(startTime,endTime,type);
        #外面一层平台遍历 里面一层景区遍历
        res = {};
        list = [];
        rrcomments = comment.objects(data_website = '携程');
        print(rrcomments.count());
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
                    rcomments = rrcomments(data_region__contains=region, comment_month=time);
                elif (type == '季度'):
                    rcomments = rrcomments(data_region__contains=region, comment_season=time);

                cnts.append(rcomments.count());

            regionRes['name'] = region;
            regionRes['data'] = cnts;
            yAxis.append(regionRes);
            websiteRes['website'] = "携程";
            websiteRes['xAxis'] = time_list;
            websiteRes['yAxis'] = yAxis;

            list.append(websiteRes);

        res['list'] = list;
        return json_response(res);











#千岛湖与其余景区同时段评论数量比较
class SpotNumComparedView(APIView):

    def post(self, request, *args, **kwargs):
        try:

            return get_spot_num_compard(request);
        except KeyError:
            return json_error(error_string="请求错误", code=500);
