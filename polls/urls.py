#!/usr/bin/ env python
# -*- coding: utf-8 -*-
# @Time      : 2018/8/13 16:56
# @Author    : yuxiang.fang
# @FileNmae  : urls..py
# @Function  :


from django.conf.urls import url
from . import views
from django.urls import path

app_name = "polls"
urlpatterns = [
    # ex: /polls/test
    url(r'^test$', views.test, name='test'),

    # # ex: /polls/
    # url(r'^index$', views.index, name='index'),
    #
    # # ex: /polls/5/
    # url(r'^(?P<question_id>[0-9]+)/detail/$', views.detail, name='detail'),
    #
    # # ex: /polls/5/results/
    # url(r'^(?P<question_id>[\d]+)/results/$', views.results, name='results'),
    #
    # # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    # 使用通用模板视图时的定义方式: path
    path('index', views.IndexView.as_view(), name='index'),
    path('<int:pk>/detail/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

    # 使用通用模板视图时的定义方式: url定义
    # url(r'^index$', views.IndexView.as_view(), name='index'),
    # url(r'^(?P<pk>[0-9]+)/detail/$', views.DetailView.as_view(), name='detail'),
    # url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
