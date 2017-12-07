from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

def getDiaryDetail(request):

    diaryID = request.path_info.split('/')[-1]

    return HttpResponse("getDiaryDetailByID:%s" % (diaryID))

def getDiarylist(request):
    return HttpResponse("getDiarylist")
