from rest_framework.views import APIView

from .CommonView import *

from ..Models.CommentModel import comment
from ..Models.InnerRegionInfoModel import innerregioninfo
from ..Models.ＣonnectToDBModel import *
import datetime
def get_user(request):
    # 进行解码token
    # username = decodeToken(request);
    # print(username);
    try:
        res = {};
        username = decodeToken(request);
        res['username'] = username;
        return json_response(res);
    except Exception:
        return json_error(error_string='查询发生错误', code=11);

class GetUserView(APIView):

    def get(self, request, *args, **kwargs):
        try:

            return get_user(request);
        except KeyError:
            return json_error(error_string="请求错误", code=500);
