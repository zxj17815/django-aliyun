# Generated by Django 2.2.3 on 2019-12-02 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aliyun_sms', '0006_smstemplate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smssign',
            name='remark',
        ),
        migrations.RemoveField(
            model_name='smssign',
            name='sign_source',
        ),
        migrations.RemoveField(
            model_name='smstemplate',
            name='remark',
        ),
        migrations.RemoveField(
            model_name='smstemplate',
            name='template_content',
        ),
        migrations.RemoveField(
            model_name='smstemplate',
            name='template_type',
        ),
        migrations.AddField(
            model_name='smstemplate',
            name='template_code',
            field=models.CharField(default='', max_length=50, verbose_name='TemplateCode'),
            preserve_default=False,
        ),
    ]