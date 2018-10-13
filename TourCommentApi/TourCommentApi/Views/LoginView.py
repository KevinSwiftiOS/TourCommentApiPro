from TourCommentApi.Models.UserModel import User
from django.contrib.auth import logout as auth_logout

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes

from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.utils import jwt_decode_handler


@api_view(('POST',))
@permission_classes((AllowAny,))
def login(request):
    print(request.POST.items())
    username = request.POST['username'];
    password = request.POST['password'];
    try:
        user_obj = User.objects.get(username = username)



    except User.DoesNotExist:
        print("create new user into table");
        user_obj = User.objects.create_user(username,
                                          '123@123.com',
                                            password);
        user_obj.save();

    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    payload = jwt_payload_handler(user_obj)

    token = jwt_encode_handler(payload)
    decode = jwt_decode_handler(token)
   # token = 111
    print(77777777)
    print(decode)
    return Response({
        'status':'验证成功',
         'token':token,
    },
        status = status.HTTP_200_OK
    );
@api_view(('POST',))
def logout(request):
    auth_logout(request)
    return Response(
        status = status.HTTP_200_OK

    )