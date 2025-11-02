# ----------------- src/apps/accounts/admin.py -----------------
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: Online Job Portal (Django)
File: src/apps/accounts/admin.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-02
Updated: 2025-11-02
License: MIT License (see LICENSE file for details)
=

Description:
Admin registration for HRProfile.

Usage:
Django admin site management.

Notes:
- Displays user and organization.

============================================================================
"""

from django.contrib import admin
from .models import HRProfile


@admin.register(HRProfile)
class HRProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "organization_name")
    search_fields = ("user__username", "organization_name")

