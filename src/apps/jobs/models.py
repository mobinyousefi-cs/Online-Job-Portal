# ----------------- models.py -----------------
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: Online Job Portal (Django)
File: src/apps/jobs/models.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-02
Updated: 2025-11-02
License: MIT License (see LICENSE file for details)
=

Description:
Data models for Job postings and Applications.

Usage:
Migrated via Django ORM.

Notes:
- Job.get_absolute_url is used in templates.

============================================================================
"""

from django.db import models
from django.urls import reverse
from apps.accounts.models import HRProfile
from .validators import validate_resume


class Job(models.Model):
    hr = models.ForeignKey(HRProfile, on_delete=models.CASCADE, related_name="jobs")
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    salary_min = models.PositiveIntegerField(null=True, blank=True)
    salary_max = models.PositiveIntegerField(null=True, blank=True)
    experience_years = models.PositiveSmallIntegerField(default=0)
    is_remote = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:  # pragma: no cover
        return self.title

    def get_absolute_url(self):
        return reverse("jobs:job_detail", args=[self.pk])


GENDER_CHOICES = (
    ("male", "Male"),
    ("female", "Female"),
    ("other", "Other"),
)


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications")
    name = models.CharField(max_length=200)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    resume = models.FileField(upload_to="resumes/", validators=[validate_resume])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:  # pragma: no cover
        return f"{self.name} → {self.job.title}"

