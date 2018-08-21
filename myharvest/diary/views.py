# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Diary
from django.template.context_processors import csrf


def getDiaryDetail(request):

    if request.method == 'GET':

        diaryID = request.path_info.split('/')[-1]
        aDiary = Diary.objects.get(id=diaryID)
        if aDiary:
            html = "<p>"+"ID:" + str(aDiary.id) + " Title:" + \
                aDiary.title + " Content:" + aDiary.content + "</p>"
            return HttpResponse(html)
        else:
            return HttpResponse("NotFound")
    return HttpResponse("error")


def getDiarylist(request):

    list = Diary.objects.all()

    html = ""
    for aDiary in list:
        html += "<p>"+"ID:" + str(aDiary.id) + " Title:" + \
            aDiary.title + " Content:" + aDiary.content + "</p>"
    return HttpResponse(html)


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


def createDiary(request):

    if request.method == 'POST':
        title = request.POST["title"]
        content = request.POST["content"]

        aDiary = Diary(title="我是标题", content="今天做了什么事情呢？？？")
        aDiary.save()
        html += "<p> 保存成功\n"+"ID:" + \
            str(aDiary.id) + " Title:" + aDiary.title + \
            " Content:" + aDiary.content + "</p>"
        return HttpResponse(html)
    return HttpResponse("createDiary  failed")
