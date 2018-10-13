from django.shortcuts import render
from rest_framework.views import APIView
import json
from django.http import HttpResponse, HttpRequest
from TourCommentApi.Models import comments
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


def json_response(data, code=200, foreign_penetrate=False, **kwargs):
    data = {
        "code": code,
        "msg": "成功",
        "data": data,
    }
    print(222222)
    users = comments.objects.all()
    # 返回所有的文档对象列表
    print(users.count())
    return response_as_json(data, foreign_penetrate=foreign_penetrate)


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
class ReturnJson(APIView):

    def get(self, request, *args, **kwargs):
        return JsonResponse("Hello world!!!!!!!!++++++中文测试")
