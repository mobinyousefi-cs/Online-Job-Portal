# ----------------- views.py -----------------
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: Online Job Portal (Django)
File: src/apps/core/views.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-02
Updated: 2025-11-02
License: MIT License (see LICENSE file for details)
=

Description:
Home view rendering a marketing landing page and featured jobs.

Usage:
GET /

Notes:
- Pulls last 6 published jobs for quick discovery.

============================================================================
"""

from django.shortcuts import render
from apps.jobs.models import Job


def index(request):
    jobs = Job.objects.filter(is_published=True).order_by("-created_at")[:6]
    return render(request, "core/index.html", {"jobs": jobs})

