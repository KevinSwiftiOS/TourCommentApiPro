from rest_framework.views import APIView

from .CommonView import *

from ..Models.CommentModel import comment
from ..Statics.Regions import *


def detail(request,id):
    print(id);
    print(request.POST['name']);
    # 返回所有的文档对象列表
    return json_error(error_string='ccc',code=100);



class DetailView(APIView):

    def post(self, request,id, *args, **kwargs):
        try:
            print(id);
            return detail(request,id);
        except KeyError:
            return json_error(error_string="请求错误", code=500);
