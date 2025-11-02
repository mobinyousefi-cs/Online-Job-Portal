# ----------------- wsgi.py -----------------
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: Online Job Portal (Django)
File: src/jobportal/wsgi.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-02
Updated: 2025-11-02
License: MIT License (see LICENSE file for details)
=

Description:
WSGI config for deployment (gunicorn/uwsgi).

Usage:
WSGI_APPLICATION = 'jobportal.wsgi.application'

Notes:
- Exposes module-level variable 'application'.

============================================================================
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jobportal.settings")
application = get_wsgi_application()
