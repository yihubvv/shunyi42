from django.shortcuts import render

# Create your views here.
"""
Views

A so-called view is actually a Python function.

A view function has two requirements:

1. The first parameter of the view function is used to receive the request. This request is actually an object of the `HttpRequest` class.

2. It must return a response.

"""
# request
from django.http import HttpRequest
from django.http import HttpResponse

# We expect the user to enter http://127.0.0.1:8000/index/
# to access the view function

def index(request):

    # return HttpResponse('ok')

    # render 渲染模板
    #request, template_name, context=None
    #request,           请求
    # template_name,    模板名字
    # context=None
    # 100/0
    #模拟数据查询
    context={
        'name':'马上双11，点击有惊喜'
    }

    return render(request,'book/index.html',context=context)
