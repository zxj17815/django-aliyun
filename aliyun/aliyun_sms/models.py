from django.db import models

# Create your models here.

class SmsUp(models.Model):
    """上行短信消息
    """
    id = models.AutoField(primary_key=True,help_text='id')
    phone_number=models.CharField(verbose_name="手机号码", max_length=50)
    send_time=models.DateTimeField(verbose_name="发送时间",auto_now=False, auto_now_add=False)
    content=models.TextField(verbose_name="发送内容")
    sign_name=models.CharField(verbose_name="签名信息", max_length=150)
    dest_code=models.CharField(verbose_name="上行短信扩展号码", max_length=150)
    sequence_id=models.IntegerField(verbose_name="序列号")

class SmsReport(models.Model):
    """上行短信消息
    """
    id = models.AutoField(primary_key=True,help_text='id')
    phone_number=models.CharField("phone_number", max_length=50)
    send_time=models.DateTimeField("send_time", auto_now=False, auto_now_add=False)
    report_time=models.DateTimeField("report_time", auto_now=False, auto_now_add=False)
    success=models.BooleanField("success")
    err_code=models.CharField("err_code", max_length=550)
    err_msg=models.CharField("err_msg", max_length=550)
    sms_size=models.CharField("sms_size", max_length=550)
    biz_id=models.CharField("biz_id", max_length=550)
    out_id=models.CharField("out_id", max_length=550)

class SmsSign(models.Model):
    """短信签名
    """
    id = models.AutoField(primary_key=True,help_text='id')
    sing_name=models.CharField("SignName", max_length=12)
    # sign_source=models.IntegerField("SignSource",choices=((0,'企事业单位的全称或简称'),(1,'工信部备案网站的全称或简称'),(2,'APP应用的全称或简称'),(3,'公众号或小程序的全称或简称'),(4,'电商平台店铺名的全称或简称'),(5,'商标名的全称或简称')))
    # remark=models.CharField("Remark", max_length=200)

class SmsTemplate(models.Model):
    """短信模板
    """
    template_name=models.CharField("TemplateName", max_length=30)
    template_code=models.CharField("TemplateCode", max_length=50)
