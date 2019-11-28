from django.urls import include, path, re_path
# 引入同级目录下的views.py文件
from . import views

app_name = 'aliyun_sms'

urlpatterns = [
    # ex: /index/
    # path('', views.wxLogin, name='wxLogin'),
    # path('requestOrder/', views.requestOrder, name='requestOrder'),
    # # ex: /index/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /index/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /index/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    path('',views.index,name='index'), # 首页
    path('send_sms/',views.send_sms,name='send_sms'), # 发送页面
    path('send_callback/', views.send_callback.as_view(), name='send_callback'), # 发送接收回调
    path('return_sms/',views.return_sms,name='return_sms'), # 回复页面
    path('return_callback/', views.return_callback.as_view(), name='return_callback'), # 回复接收回调
    
]
