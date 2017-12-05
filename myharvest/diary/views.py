from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse

def getDiary(request):
    return HttpResponse("getDiary")

def getDiarys(request):
    return HttpResponse("getDiarys")
