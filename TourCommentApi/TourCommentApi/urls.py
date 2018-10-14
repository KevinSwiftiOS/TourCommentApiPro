"""TourCommentApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from rest_framework.schemas import get_schema_view
from rest_framework_jwt.views import obtain_jwt_token

from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token


from rest_framework.routers import DefaultRouter




from .Views.LoginView import login


from .Views.JingquListView import JingquListView
from .Views.JingdianListView import JingdianListView
from .Views.JingquCountView import JingquCountView
from .Views.jingquDetailView import JingquDetailView
from .Views.JingquDymanicCommentView import jingquDymanicCommentView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', get_schema_view()),
    #登录接口
    url(r'^api/login$',login),
    #首页获取全部信息接口
    url(r'^api/jingqulist', JingquListView.as_view()),
    #获取景点详情
    url(r'^api/jingdianlist/(?P<id>[0-9A-Fa-f-]+)', JingdianListView.as_view()),
    #获取景区的统计数目  首页————某某其余5A级景区
    url(r'^api/jingqucount/(?P<id>[0-9A-Fa-f-]+)', JingquCountView.as_view()),
     #景区的详细分析
    url(r'^api/jingqudetail/(?P<id>[0-9A-Fa-f-]+)', JingquDetailView.as_view()),
    #景区动态页面
    url(r'^api/jingquDymanicComment', jingquDymanicCommentView.as_view()),

]

