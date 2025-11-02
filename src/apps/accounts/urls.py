# ----------------- urls.py -----------------
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: Online Job Portal (Django)
File: src/apps/accounts/urls.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-02
Updated: 2025-11-02
License: MIT License (see LICENSE file for details)
=

Description:
Routes for HR login/registration/logout.

Usage:
Included at /accounts/

Notes:
- Namespaced as 'accounts'.

============================================================================
"""

from django.urls import path
from .views import HRLoginView, HRLogoutView, register

urlpatterns = [
    path("login/", HRLoginView.as_view(), name="login"),
    path("logout/", HRLogoutView.as_view(), name="logout"),
    path("register/", register, name="register"),
]

