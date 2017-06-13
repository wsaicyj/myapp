#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import update_list
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    # url(r"^$", TemplateView.as_view(template_name="update_list.html")),
    url(r"^$", update_list, name='update_list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)