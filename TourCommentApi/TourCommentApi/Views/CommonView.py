

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


#获取时间颗粒度
def get_time_list(startTime,endTime,type):
    start_year = int(startTime.split('-')[0]);
    start_date = int(startTime.split('-')[1]);
    end_year = int(endTime.split('-')[0]);
    end_date = int(endTime.split('-')[1]);
    #截止时间 月截止到13 季度截止到5 方便后面一个遍历
    if(type == '月'):
        end_time = 13;
    elif(type == '季度'):
        end_time = 5;
    time_list = [];

    # 开始结束年份不同 需将月份加上
    if (start_year < end_year):
        first = True;
        for year in range(start_year, end_year + 1):
            if (year != end_year):
                if (first):
                    first = False;
                    for month in range(start_date, end_time):
                        time_list.append(str(year) + '-' + str(month).zfill(2));
                else:
                    for month in range(1, end_time):
                        time_list.append(str(year) + '-' + str(month).zfill(2));
            else:
                for month in range(1, end_date + 1):
                    time_list.append(str(year) + '-' + str(month).zfill(2));
    # 开始结束年份相同 只需遍历日期即可
    else:
        for month in range(start_date, end_date + 1):
            time_list.append(str(start_year) + '-' + str(month).zfill(2));


    return time_list;
