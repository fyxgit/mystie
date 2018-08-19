#!/usr/bin/ env python
# -*- coding: utf-8 -*-
# @Time      : 2018/8/12 22:02
# @Author    : yuxiang.fang
# @FileNmae  : urls..py
# @Function  :


from cmdb import views
from django.urls import path

urlpatterns = [
    path('contact/', views.contact),
    path('database/', views.database),
]
