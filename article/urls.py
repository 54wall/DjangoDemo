from django.urls import path
from django.views.generic import RedirectView

from article.views import TestView

urlpatterns = [

    # path('test', TestView.as_view(), name='test'),  # 测试

    path('', RedirectView.as_view(url='user/login.html')),

]
