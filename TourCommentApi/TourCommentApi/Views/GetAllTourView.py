from rest_framework.views import APIView
import json
from django.http import HttpResponse
from TourCommentApi.Models.models import comments
from TourCommentApi.Statics.regions import regions
import re
from rest_framework_jwt.utils import jwt_decode_handler
# Create your views here.
def response_as_json(data,foreign_penetrate = False):
    #防止中文转化为unicode编码
    jsonString = json.dumps(data,ensure_ascii=False)
    response = HttpResponse(
        jsonString,
        content_type='application/json'
    )
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response


def json_response( code=0, foreign_penetrate=False, **kwargs):
    res = {

    }
    
    datas = []
    for region in (regions):
        comment = comments.objects(data_region = region)
        data = {
            'data_region':region,
             'comment_count':comment.count(),
              'comment_score':round(comment.average('comment_score'),1)
            #差一个排名
        }
        datas.append(data)
        # datas.sort(reverse=True, key=lambda student: student[1])
        #所有评分的合计
    res['code'] = 0;
    res['data'] = datas;
    res['msg'] = ''


    # 返回所有的文档对象列表
   
    return response_as_json(res, foreign_penetrate=foreign_penetrate)


def json_error(error_string="", code=500, **kwargs):
    data = {
        "code": code,
        "msg": error_string,
        "data": {}
    }
    data.update(kwargs)
    return response_as_json(data)

JsonResponse = json_response
JsonError = json_error
class GetAllTourView(APIView):

    def post(self, request, *args, **kwargs):
        try:

         token =  request.META['HTTP_AUTHORIZATION']
         #(re.findall(r'\s.*',token)[0].strip())
         decode = jwt_decode_handler(re.findall(r'\s.*',token)[0].strip())
         print(decode['username'])
         return JsonResponse()
        except KeyError:
            print(11111)