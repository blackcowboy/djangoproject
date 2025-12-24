from django.shortcuts import render

# Create your views here.
from public.util.MsgUtil import ResponseUtil


def index(request):
    return ResponseUtil.ResultOK('index页面')