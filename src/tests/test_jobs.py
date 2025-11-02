#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: Online Job Portal (Django)
File: src/tests/test_jobs.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-02
Updated: 2025-11-02
License: MIT License (see LICENSE file for details)
=

Description:
Smoke tests for Job CRUD and public list.

Usage:
pytest -q

Notes:
- Uses Django test client.

============================================================================
"""

import io
import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from apps.accounts.models import HRProfile
from apps.jobs.models import Job


@pytest.fixture
def hr_user(db):
    user = User.objects.create_user(username="hr2", password="pass1234", email="hr2@example.com")
    HRProfile.objects.create(user=user, organization_name="Globex")
    return user


@pytest.mark.django_db
def test_job_crud_and_apply(client, hr_user):
    # Login HR
    client.login(username="hr2", password="pass1234")

    # Create job
    resp = client.post(reverse("jobs:job_create"), {
        "title": "Backend Engineer",
        "description": "Django + APIs",
        "location": "Remote",
        "salary_min": 1000,
        "salary_max": 2000,
        "experience_years": 2,
        "is_remote": True,
        "is_published": True,
    })
    assert resp.status_code in (302, 200)
    job = Job.objects.get(title="Backend Engineer")

    # Public apply
    resume = io.BytesIO(b"dummy pdf content")
    resume.name = "resume.pdf"
    resp = client.post(reverse("jobs:apply", args=[job.pk]), {
        "name": "Alice Applicant",
        "dob": "1995-01-01",
        "gender": "female",
        "mobile": "+1-555-0100",
        "email": "alice@example.com",
    }, format='multipart')
    # Missing file -> should render with errors
    assert resp.status_code == 200
