from rest_framework.views import APIView

from .CommonView import *

from ..Models.CommentModel import comment
from ..Models.RegionInfoModel import regioninfo

import datetime

def get_jingqu_dymanic_comment(request,id):
    # #post中拿到景区列表 和开始结束时间
    # search_keys = request.POST['regions'];
    # start = request.POST['start'];
    # end = request.POST['end'];
    # websites = request.POST['websites'];
    # #
    #
    # #将本月新增评论取出 进行过滤查询
    #     #获取当月
    # #默认以2位进行对齐
    # year_month = str(datetime.datetime.now().year) + '-' +   str(datetime.datetime.now().month).zfill(2);
    # print(year_month);
    # try:
    #     comments = comment.objects(data_region__contains =  data_region.get().search_key,comment_time__contains = year_month);
    #
    #     data = {
    #          'month':comments.count(),
    #           'score':round(comments.average('comment_score'),1),
    #
    #           #经纬度后期再加上
    #
    #         #差一个排名
    #     };
    #     list.append(data);
    #
    # except comments.DoesNotExist:
    #     print(2222222)
        return json_error(error_string='发生内部错误', code=11);

    # 返回所有的文档对象列表
    # res['list'] = list;
    # return json_response(res);





class jingquDymanicCommentView(APIView):

    def post(self, request, *args, **kwargs):
        try:

            return get_jingqu_dymanic_comment(request);
        except KeyError:
            return json_error(error_string="请求错误", code=500);
