# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from userinfo.models import Character

def profile(request):
    return HttpResponse("profile")

def staff(request):
    # return HttpResponse("staff")
    method = request.method
    queryDic = request.GET
    staff_list = Character.objects.all()
    # 输出所有数据
    staff_str = ""
    for var in staff_list:
        staff_str += "<p>" + var.name + "</p>"
    return HttpResponse("<div>" + staff_str + "</div>")