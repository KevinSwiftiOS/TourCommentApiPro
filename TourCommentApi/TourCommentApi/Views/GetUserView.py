from rest_framework.views import APIView
from .CommonView import *
def get_user(request):
    # 进行解码token
    # username = decodeToken(request);
    # print(username);
    try:
        #获取用户信息
        res = {};
        username = decodeToken(request);
        res['username'] = username;
        return json_response(res);
    except Exception:
        return json_error(error_string='获取用户信息失败', code=11,api='getuser');

class GetUserView(APIView):

    def get(self, request, *args, **kwargs):
        try:

            return get_user(request);
        except KeyError:
            return json_error(error_string="请求错误", code=500);
