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

# render renders the template
# request, template_name, context=None
# request,           the request
# template_name,     the template name
# context=None
# 100/0
# simulate a data query

# update the data in the template dynamically through the context parameter
    context={
        'name':'Python Django Book',
    }

    return render(request,'book/index.html',context=context)
