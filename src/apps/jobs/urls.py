# ----------------- urls.py -----------------
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: Online Job Portal (Django)
File: src/apps/jobs/urls.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-02
Updated: 2025-11-02
License: MIT License (see LICENSE file for details)
=

Description:
Route map for job browsing and HR CRUD.

Usage:
Included at /jobs/

Notes:
- Namespaced as 'jobs'.

============================================================================
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.job_list, name="job_list"),
    path("mine/", views.job_mine, name="job_mine"),
    path("create/", views.job_create, name="job_create"),
    path("<int:pk>/", views.job_detail, name="job_detail"),
    path("<int:pk>/apply/", views.apply, name="apply"),
    path("<int:pk>/edit/", views.job_update, name="job_update"),
]

