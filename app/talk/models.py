#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Talk(models.Model):
    """
    说说的数据表结构
    """
    user = models.CharField(max_length=20)
    content = models.CharField(max_length=500)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    time = models.TimeField()

    def __str__(self):
        return self.content
