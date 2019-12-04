from django import template
from .. import models
from django.apps import apps
from django.contrib.auth.models import User


register=template.Library()

@register.simple_tag
def get_model_fields_name(model,field_name):
    """
    Returns verbose_name for a field.
    返回model的字段
    在template里使用方法：
        {% get_model_fields_name 'model' 'field_name' %}
    """
    modelobj = apps.get_model('aliyun_sms', model)
    return modelobj._meta.get_field(field_name).verbose_name.title()