# ----------------- services.py -----------------
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: Online Job Portal (Django)
File: src/apps/jobs/services.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-02
Updated: 2025-11-02
License: MIT License (see LICENSE file for details)
=

Description:
Service helpers for filtering and notifications.

Usage:
Used in list view and application submission.

Notes:
- Email backend is console by default.

============================================================================
"""

from typing import Dict
from django.core.mail import send_mail
from django.db.models import Q
from .models import Job


def filter_jobs(params: Dict[str, str]):
    qs = Job.objects.filter(is_published=True)
    q = params.get("q")
    location = params.get("location")
    min_exp = params.get("min_exp")
    remote = params.get("remote")

    if q:
        qs = qs.filter(Q(title__icontains=q) | Q(description__icontains=q))
    if location:
        qs = qs.filter(location__icontains=location)
    if min_exp:
        try:
            qs = qs.filter(experience_years__gte=int(min_exp))
        except ValueError:
            pass
    if remote == "1":
        qs = qs.filter(is_remote=True)
    return qs


def notify_hr_application(application):
    job = application.job
    subject = f"New applicant for {job.title}"
    body = (
        f"Name: {application.name}\nEmail: {application.email}\nMobile: {application.mobile}\n"
        f"Resume: {application.resume.url}"
    )
    send_mail(subject, body, None, [job.hr.user.email], fail_silently=True)

