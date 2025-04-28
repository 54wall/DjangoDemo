from django.urls import path

from article.views import TestView

urlpatterns = [

    path('test', TestView.as_view(), name='test'),  # 测试
]
