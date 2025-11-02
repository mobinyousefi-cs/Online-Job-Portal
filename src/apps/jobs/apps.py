# ----------------- apps.py -----------------
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: Online Job Portal (Django)
File: src/apps/jobs/apps.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-02
Updated: 2025-11-02
License: MIT License (see LICENSE file for details)
=

Description:
App config for Jobs.

Usage:
Listed in INSTALLED_APPS.

Notes:
- Default config.

============================================================================
"""

from django.apps import AppConfig


class JobsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.jobs"

