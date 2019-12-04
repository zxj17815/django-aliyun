import json
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from . import models

class SmsUpSerializer(serializers.ModelSerializer):
    """SmsUp
    """
    send_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = models.SmsUp
        fields = '__all__'
        # exclude = ['user',]
        depth = 1
        extra_kwargs = {
            'sign_name': {'required':False},
        }

class SmsReportSerializer(serializers.ModelSerializer):
    """SmsRepor
    """
    send_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    report_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = models.SmsReport
        fields = '__all__'
        # exclude = ['user',]
        depth = 1
        extra_kwargs = {
            'out_id': {'required':False},
        }

class SmsSignSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SmsSign
        fields = '__all__'

class SmsTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SmsTemplate
        fields = '__all__'