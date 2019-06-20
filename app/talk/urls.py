#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    urls.py
   @Desc:     
   @Author:   Asura  liangz.org@gmail.com
   @Create:   2019.06.20   21:34
-------------------------------------------------------------------------------
   @Change:   2019.06.20
-------------------------------------------------------------------------------
"""

from django.conf.urls import url
from app.talk import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


