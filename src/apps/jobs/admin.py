#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: Online Job Portal (Django)
File: src/apps/jobs/admin.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-02
Updated: 2025-11-02
License: MIT License (see LICENSE file for details)
=

Description:
Admin registrations for Job and Application models.

Usage:
Django admin site management.

Notes:
- Adds list filters and search.

============================================================================
"""

from django.contrib import admin
from .models import Job, Application


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("title", "location", "experience_years", "is_remote", "is_published", "created_at")
    list_filter = ("is_published", "is_remote", "experience_years")
    search_fields = ("title", "description", "location")


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("name", "job", "email", "created_at")
    list_filter = ("gender", "created_at")
    search_fields = ("name", "email", "mobile")
