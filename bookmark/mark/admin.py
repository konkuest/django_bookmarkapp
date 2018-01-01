# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from mark.models import Bookmark #Added

# Register your models here.

# Added for defining BookmarkAdmin
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')

# Added for register
admin.site.register(Bookmark, BookmarkAdmin)