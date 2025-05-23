from django.urls import path

from user.views import toLoginPage, toRegisterPage

urlpatterns = [

    path('login.html', toLoginPage, name='toLoginPage'),
    path('register.html', toRegisterPage, name='toRegisterPage'),

]
