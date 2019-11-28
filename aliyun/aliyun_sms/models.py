from django.db import models

# Create your models here.

class SmsUp(models.Model):
    """上行短信消息
    """
    id = models.AutoField(primary_key=True,help_text='id')
    phone_number=models.CharField("phone_number", max_length=50)
    send_time=models.DateTimeField("send_time",auto_now=False, auto_now_add=False)
    content=models.TextField("content")
    sign_name=models.CharField("sign_name", max_length=150)
    dest_code=models.CharField("dest_code", max_length=150)
    sequence_id=models.IntegerField("sequence_id")

class SmsReport(models.Model):
    """上行短信消息
    """
    id = models.AutoField(primary_key=True,help_text='id')
    phone_number=models.CharField("phone_number", max_length=50)
    send_time=models.DateTimeField("send_time", auto_now=False, auto_now_add=False)
    report_time=models.DateTimeField("report_time", auto_now=False, auto_now_add=False)
    success=models.BooleanField("success")
    err_code=models.CharField("err_code", max_length=150)
    err_msg=models.CharField("err_msg", max_length=150)
    sms_size=models.CharField("sms_size", max_length=150)
    biz_id=models.CharField("biz_id", max_length=150)
    out_id=models.CharField("out_id", max_length=150)