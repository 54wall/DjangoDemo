from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from article.models import ArticleType


# Create your views here.
class TestView(View):
    def get(self, request):
        # articleTypeList_obj = ArticleType.objects.all()
        # print(articleTypeList_obj, type(articleTypeList_obj))
        # articleTypeList_dict = articleTypeList_obj._values()  # 转存字典
        # print(articleTypeList_dict, type(articleTypeList_dict))
        # articleTypeList = list(articleTypeList_dict)
        # print(articleTypeList, type(articleTypeList))
        # return JsonResponse({'code': 200, 'info': '测试！'})

        return render(request, 'test.html')
