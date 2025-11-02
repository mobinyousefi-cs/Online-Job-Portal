# ----------------- views.py -----------------
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: Online Job Portal (Django)
File: src/apps/accounts/views.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-02
Updated: 2025-11-02
License: MIT License (see LICENSE file for details)
=

Description:
Authentication views for HR users.

Usage:
/register/ and /login/

Notes:
- Uses Django auth views for login/logout.

============================================================================
"""

from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import HRRegisterForm


class HRLoginView(LoginView):
    template_name = "accounts/login.html"


class HRLogoutView(LogoutView):
    next_page = reverse_lazy("core:index")


def register(request):
    if request.method == "POST":
        form = HRRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created. Please log in.")
            return redirect("accounts:login")
    else:
        form = HRRegisterForm()
    return render(request, "accounts/register.html", {"form": form})

