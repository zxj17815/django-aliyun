import datetime
import json
from venv import create

import requests
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend  # 通用过滤器
from rest_framework import permissions  # 权限
from rest_framework import status  # 状态码
from rest_framework import generics, views, viewsets
from rest_framework.decorators import parser_classes, renderer_classes
from rest_framework.parsers import *  # 解析器
from rest_framework.response import Response  # 返回
from rest_framework.versioning import URLPathVersioning  # api版本控制

#aliyun
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

from . import serializers  # 自定义的序列化类
from . import models

# Create your views here.


def index(request):
    # now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)
    return render(request, 'index.html')


def send_sms(request):
    """短信发送"""
    client = AcsClient('<accessKeyId>', '<accessSecret>', 'cn-hangzhou')

    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https') # https | http
    request.set_version('2017-05-25')
    request.set_action_name('SendBatchSms')

    request.add_query_param('RegionId', "cn-hangzhou")
    request.add_query_param('PhoneNumberJson', "[\"15900000000\",\"13500000000\"]")
    request.add_query_param('SignNameJson', "[\"阿里云\",\"阿里巴巴\"]")
    request.add_query_param('TemplateCode', "SMS_152550005")
    request.add_query_param('TemplateParamJson', "[{\"name\":\"TemplateParamJson\"},{\"name\":\"TemplateParamJson\"}]")

    response = client.do_action(request)
    # python2:  print(response) 
    print(str(response, encoding = 'utf-8'))


class send_callback(views.APIView):
    """上行回调接口"""
    def post(self, request, *args, **kwargs):
        for data in request.data:
            serializer=serializers.SmsReportSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response({
            "code": 0,
            "msg": "成功"
        })

def return_sms(request):
    pass

class return_callback(views.APIView):
    def post(self, request, *args, **kwargs):
        for data in request.data:
            serializer=serializers.SmsUpSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response({
            "code": 0,
            "msg": "成功"
        })
        # return Response(serializer.data)
