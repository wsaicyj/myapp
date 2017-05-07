#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import archive

urlpatterns = [
    # url(r'^$', archive, name='archive')
    url(r'^archives/(?P<year>\d{4})/(?P<day>\d{2})/$', archive, name='archive')
]