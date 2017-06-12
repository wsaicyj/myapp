#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from django.conf.urls import url
from livelog.models import Update


urlpatterns = [url(r"^$", 'list_detail.object_list', {'queryset': Update.objects.all()})]