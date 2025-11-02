#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: Online Job Portal (Django)
File: src/tests/test_accounts.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-02
Updated: 2025-11-02
License: MIT License (see LICENSE file for details)
=

Description:
Smoke tests for HR registration/login.

Usage:
pytest -q

Notes:
- Minimal e2e using Django test client.

============================================================================
"""

import pytest
from django.urls import reverse
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_hr_register_and_login(client):
    # Register
    resp = client.post(reverse("accounts:register"), {
        "username": "hr1",
        "email": "hr1@example.com",
        "password": "pass1234",
        "organization_name": "ACME",
    })
    assert resp.status_code in (302, 200)

    # Login
    resp = client.post(reverse("accounts:login"), {"username": "hr1", "password": "pass1234"})
    assert resp.status_code in (302, 200)
    assert User.objects.filter(username="hr1").exists()