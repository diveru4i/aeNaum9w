# -*- coding: utf-8 -*-
from django.urls import path

from core.views import IndexView, FindView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('all/', FindView.as_view(method_name='get_flights'), name='all'),
    path('best/', FindView.as_view(method_name='get_best'), name='best'),
]

