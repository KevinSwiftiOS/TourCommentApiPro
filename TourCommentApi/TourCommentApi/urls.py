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
from TourCommentApi.Views.LoginView import logout,login

from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'user',views.UserViewSet)


from .Views.GetAllTourView import GetAllTourView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', get_schema_view()),
   # url(r'^api/',include(router.urls))
    url(r'^login/$',login),
    url(r'^logout/$',logout),
    # url(r'^api-token-auth/',obtain_jwt_token),
    # url(r'^api-token-refresh/', refresh_jwt_token),
    # url(r'^api-token-verify/', verify_jwt_token),
    url(r'^api/getAllTour', GetAllTourView.as_view()),
]

