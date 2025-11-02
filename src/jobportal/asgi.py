# ----------------- asgi.py -----------------
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: Online Job Portal (Django)
File: src/jobportal/asgi.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-02
Updated: 2025-11-02
License: MIT License (see LICENSE file for details)
=

Description:
ASGI config for async servers (uvicorn/daphne).

Usage:
ASGI_APPLICATION = 'jobportal.asgi.application'

Notes:
- Exposes module-level variable 'application'.

============================================================================
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jobportal.settings")
application = get_asgi_application()
