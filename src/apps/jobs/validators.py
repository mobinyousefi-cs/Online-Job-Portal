# ----------------- validators.py -----------------
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: Online Job Portal (Django)
File: src/apps/jobs/validators.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-02
Updated: 2025-11-02
License: MIT License (see LICENSE file for details)
=

Description:
File validators for resumes.

Usage:
Imported in Application model.

Notes:
- Uses settings for allowed extensions and size.

============================================================================
"""

import os
from django.conf import settings
from django.core.exceptions import ValidationError


def validate_resume(file):
    max_bytes = settings.MAX_UPLOAD_MB * 1024 * 1024
    if file.size > max_bytes:
        raise ValidationError(f"File too large (>{settings.MAX_UPLOAD_MB}MB)")
    ext = os.path.splitext(file.name)[1].lower()
    if ext not in settings.ALLOWED_RESUME_TYPES:
        raise ValidationError("Unsupported file type. Allowed: " + ", ".join(settings.ALLOWED_RESUME_TYPES))

