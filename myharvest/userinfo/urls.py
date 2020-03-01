# -*- coding:utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^profile', views.profile),
    url(r'^staff', views.staff),
]