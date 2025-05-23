from django.shortcuts import render


# Create your views here.
def toLoginPage(request):
    return render(request, 'login.html')


def toRegisterPage(request):
    return render(request, 'register.html')
