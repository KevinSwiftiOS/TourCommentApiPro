# -*- coding: utf-8 -*-
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


import time



from .Views.LoginView import login


from .Views.SpotListView import SpotListView
from .Views.QdhSpotListView import QdhSpotListView
from .Views.SpotDetailView import SpotDetailView
# from .Views.jingquDetailView import JingquDetailView
# from .Views.JingquDymanicCommentView import jingquDymanicCommentView
from .Views.SpotComparedView import SpotComparedView
from .Views.QdhStateView import QdhStateView
from .Views.GetUserView import GetUserView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', get_schema_view()),
    #登录接口
    url(r'^api/login$',login),
    #首页获取全部信息接口
    url(r'^api/spotlist', SpotListView.as_view()),
    #获取景点详情
    url(r'^api/qdhspotlist', QdhSpotListView.as_view()),
    #获取景区的统计数目  首页————某某其余5A级景区
    url(r'^api/spotdetail/(?P<id>[0-9A-Fa-f-]+)', SpotDetailView.as_view()),
     #景区的详细分析
    # url(r'^api/jingqudetail/(?P<id>[0-9A-Fa-f-]+)', JingquDetailView.as_view()),
    #千岛湖景区与其余景区进行比较　评论数
    url(r'^api/spotcompared', SpotComparedView.as_view()),
    # 千岛湖景区动态
    url(r'^api/qdhstate', QdhStateView.as_view()),
    # 获取用户个人信息
    url(r'^api/getuser', GetUserView.as_view()),
]

