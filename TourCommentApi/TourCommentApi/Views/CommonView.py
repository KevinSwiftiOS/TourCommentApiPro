

import json
from django.http import HttpResponse
from rest_framework_jwt.utils import jwt_decode_handler
import re,logging
#公用的一些方法
def response_as_json(data, foreign_penetrate=False):
    # 防止中文转化为unicode编码
    jsonString = json.dumps(data, ensure_ascii=False)
    response = HttpResponse(
        jsonString,
        content_type='application/json'
    )
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

def json_error(error_string="", code=500, **kwargs):
    data = {
        "code": code,
        "message": error_string,
        "data": {}
    }
    logger = logging.getLogger('django')
    logger.info('This is an errormsg')
    return response_as_json(data)

def json_response(data,code=0, foreign_penetrate=False, **kwargs):
     res = {};
     res['data'] = data;
     res['message'] = "";
     res['code'] = 0;
     return response_as_json(res);

#进行解码的token
def decodeToken(request):

    token = request.META['HTTP_AUTHORIZATION'];
    # (re.findall(r'\s.*',token)[0].strip())
    decode = jwt_decode_handler(re.findall(r'\s.*', token)[0].strip());

    return decode['username'];
