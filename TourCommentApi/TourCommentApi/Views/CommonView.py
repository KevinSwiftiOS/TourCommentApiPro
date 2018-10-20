
# -*- coding: utf-8 -*-
import pandas as pd
import json
from django.http import HttpResponse
from rest_framework_jwt.utils import jwt_decode_handler
import re,logging
import datetime
import numpy as np;
from ..Models.ConnectToDBModel import *
#编码为json
def response_as_json(data, foreign_penetrate=False):
    # 防止中文转化为unicode编码
    jsonString =  pd.io.json.dumps(data, ensure_ascii=False)
    response = HttpResponse(
        jsonString,
        content_type='application/json',
        charset='utf-8'
    )
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    #response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response
#错误返回
def json_error(error_string="", code=500,api = "",**kwargs):
    data = {
        "code": code,
        "message": error_string,
        "data": {}
    }
    logger = logging.getLogger('django')
    #时间
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    logger.info('时间:' + str(time) + ' 错误信息:' + error_string + " code:" + str(code) + "接口为:" + api);
    return response_as_json(data);
#正常返回
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
def get_time_list(startTime,endTime,time):
    start_year = int(startTime.split('-')[0]);
    start_date = int(startTime.split('-')[1]);
    end_year = int(endTime.split('-')[0]);
    end_date = int(endTime.split('-')[1]);

    #截止时间 月截止到13 季度截止到5 周截止到53 方便后面一个遍历
    end_time_keys = {
        '月':13,
        '季度':5,
        '周':53,
        '年':2018
    };

    end_time = end_time_keys[time];

    time_list = [];
    #排序不是年份
    if(time != '年'):
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
    else:
        time_list = [str(year) for year in range(start_year,end_year + 1)];

    return time_list;


#获取排名

def get_rank(key):
    return (get_spot_ranks_dic())[key];

#获取平均分，为np.nan的时候返回0
def get_score(score):
    if score is np.nan:
        return 0;
    else:
       return round(score,1);

