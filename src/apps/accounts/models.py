# ----------------- models.py -----------------
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: Online Job Portal (Django)
File: src/apps/accounts/models.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-02
Updated: 2025-11-02
License: MIT License (see LICENSE file for details)
=

Description:
HRProfile model extending Django's auth.User via OneToOne.

Usage:
Used to link jobs to the HR and store organization name.

Notes:
- Signals could be added later to auto-create profiles.

============================================================================
"""

from django.db import models
from django.contrib.auth.models import User


class HRProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="hr_profile")
    organization_name = models.CharField(max_length=255)

    def __str__(self) -> str:  # pragma: no cover - trivial
        return f"{self.organization_name} ({self.user.username})"

