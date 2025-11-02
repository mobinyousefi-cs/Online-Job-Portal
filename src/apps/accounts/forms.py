# ----------------- forms.py -----------------
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: Online Job Portal (Django)
File: src/apps/accounts/forms.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-02
Updated: 2025-11-02
License: MIT License (see LICENSE file for details)
=

Description:
Registration form for HR combining User and HRProfile fields.

Usage:
Used by RegisterView.

Notes:
- Basic validation for unique username/email.

============================================================================
"""

from django import forms
from django.contrib.auth.models import User
from .models import HRProfile


class HRRegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    organization_name = forms.CharField(max_length=255)

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already taken")
        return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already registered")
        return email

    def save(self):
        data = self.cleaned_data
        user = User.objects.create_user(
            username=data["username"], email=data["email"], password=data["password"]
        )
        HRProfile.objects.create(user=user, organization_name=data["organization_name"])
        return user

