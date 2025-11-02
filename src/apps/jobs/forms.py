# ----------------- forms.py -----------------
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: Online Job Portal (Django)
File: src/apps/jobs/forms.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-02
Updated: 2025-11-02
License: MIT License (see LICENSE file for details)
=

Description:
Forms for Job creation (HR) and Application (public).

Usage:
Used in corresponding views.

Notes:
- Clean salary range.

============================================================================
"""

from django import forms
from .models import Job, Application


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            "title",
            "description",
            "location",
            "salary_min",
            "salary_max",
            "experience_years",
            "is_remote",
            "is_published",
        ]

    def clean(self):
        data = super().clean()
        smin, smax = data.get("salary_min"), data.get("salary_max")
        if smin and smax and smin > smax:
            raise forms.ValidationError("Minimum salary cannot exceed maximum salary")
        return data


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["name", "dob", "gender", "mobile", "email", "resume"]

