from django.urls import path
from book.views import index
# This is the fixed writing pattern urlpatterns = []
urlpatterns = [
    # path(route, view_function_name)
    path('index/',index),
    ]