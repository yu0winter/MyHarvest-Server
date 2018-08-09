# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import Diary
from django.template.context_processors import csrf


def getDiaryDetail(request):
    list = Diary.objects.all()
    print (list.count())


    diaryID = request.path_info.split('/')[-1]
    return HttpResponse("getDiaryDetailByID:%s" % (diaryID))

def getDiarylist(request):
    return HttpResponse("getDiarylist")


# def investigate(request):
#     if request.POST:
#         submitted  = request.POST['staff']
#         new_record = Character(name = submitted)
#         new_record.save()
#     ctx ={}
#     ctx.update(csrf(request))
#     all_records = Character.objects.all()
#     ctx['staff'] = all_records
#     return render(request, "investigate.html", ctx)


def createDiary(reqeust):

    aDiary = Diary(title="我是标题",content="今天做了什么事情呢？？？")
    aDiary.save()


    ctx = {}
    ctx.update(csrf(request))

    return HttpResponse("createDiary")