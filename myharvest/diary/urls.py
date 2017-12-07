# -*- coding:utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    #
    url(r'^[0-9]{1,9}', views.getDiaryDetail),
    url(r'^list/', views.getDiarylist),
]