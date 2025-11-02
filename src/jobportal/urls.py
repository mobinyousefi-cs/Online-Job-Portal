# ----------------- urls.py -----------------
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: Online Job Portal (Django)
File: src/jobportal/urls.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-02
Updated: 2025-11-02
License: MIT License (see LICENSE file for details)
=

Description:
Root URL configuration.

Usage:
Included by Django runtime.

Notes:
- Serves media in DEBUG mode only.

============================================================================
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.core.urls")),
    path("accounts/", include(("apps.accounts.urls", "accounts"), namespace="accounts")),
    path("jobs/", include(("apps.jobs.urls", "jobs"), namespace="jobs")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
