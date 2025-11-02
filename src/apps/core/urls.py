# ----------------- urls.py -----------------
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: Online Job Portal (Django)
File: src/apps/core/urls.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-02
Updated: 2025-11-02
License: MIT License (see LICENSE file for details)
=

Description:
Core routes for the homepage.

Usage:
Included at root path.

Notes:
- Landing page shows featured jobs.

============================================================================
"""

from django.urls import path
from .views import index

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
]

