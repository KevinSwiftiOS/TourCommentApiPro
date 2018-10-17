
# -*- coding: utf-8 -*-

from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework_jwt.settings import api_settings
from ..Models.UserModel import user
from .CommonView import *

@api_view(('POST',))
@permission_classes((AllowAny,))
def login(request):
    login_user = json.loads(request.body);

    username = login_user['username'];
    password = login_user['password'];


    # 从数据库中进行查找
    try:
        users = user.objects.get(username=username);
        if (users.password != password):
            return json_error(error_string='用户密码错误', code=10);
        else:

            data = {};
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER;
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER;
            payload = jwt_payload_handler(users);
            token = jwt_encode_handler(payload);
            data['token'] = token;

            return json_response(data);
    except user.DoesNotExist:
        return json_error(error_string='用户不存在', code=9);
