#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'

from django.conf.urls import url
# from django.contrib import admin
from .views import index
from django.conf.urls.static import static
# from django.conf import settings
from myapp import settings

urlpatterns = [
    url(r'^$', index, name='index')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
