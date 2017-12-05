# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return HttpResponse("login")

def logout(request):
    return HttpResponse("logout")

def register(request):
    return HttpResponse("register")

def changepassword(request):
    return HttpResponse("changepassword")

def forgetpassword(request):
    return HttpResponse("forgetpassword")
