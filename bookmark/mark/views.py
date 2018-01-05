# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import ListView, DetailView
from mark.models import Bookmark

# Create your views here.

#List View - 제네릭뷰를 상속받아서 BookmarkLV 생성
class BookmarkLV(ListView):
    model = Bookmark

#Detail View - 제네릭뷰를 상속받아서 BookmarkDV 생성
class BookmarkDV(DetailView):
    model = Bookmark

