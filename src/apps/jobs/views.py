# ----------------- views.py -----------------
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: Online Job Portal (Django)
File: src/apps/jobs/views.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-02
Updated: 2025-11-02
License: MIT License (see LICENSE file for details)
=

Description:
Public job listing/detail/apply and HR CRUD views.

Usage:
See urls.py for route map.

Notes:
- Job seekers do not need authentication to apply.

============================================================================
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Job
from .forms import JobForm, ApplicationForm
from .services import filter_jobs, notify_hr_application


# Public

def job_list(request):
    qs = filter_jobs(request.GET)
    paginator = Paginator(qs, 10)
    page = request.GET.get("page")
    jobs = paginator.get_page(page)
    return render(request, "jobs/job_list.html", {"jobs": jobs})


def job_detail(request, pk: int):
    job = get_object_or_404(Job, pk=pk, is_published=True)
    form = ApplicationForm()
    return render(request, "jobs/job_detail.html", {"job": job, "form": form})


def apply(request, pk: int):
    job = get_object_or_404(Job, pk=pk, is_published=True)
    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            notify_hr_application(application)
            messages.success(request, "Application submitted successfully.")
            return render(request, "jobs/application_submitted.html", {"job": job})
    else:
        form = ApplicationForm()
    return render(request, "jobs/job_detail.html", {"job": job, "form": form})


# HR (protected)

@login_required
def job_create(request):
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.hr = request.user.hr_profile  # type: ignore[attr-defined]
            job.save()
            messages.success(request, "Job created.")
            return redirect(job.get_absolute_url())
    else:
        form = JobForm()
    return render(request, "jobs/job_form.html", {"form": form, "title": "Post a Job"})


@login_required
def job_update(request, pk: int):
    job = get_object_or_404(Job, pk=pk, hr=request.user.hr_profile)  # type: ignore[attr-defined]
    if request.method == "POST":
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, "Job updated.")
            return redirect(job.get_absolute_url())
    else:
        form = JobForm(instance=job)
    return render(request, "jobs/job_form.html", {"form": form, "title": "Edit Job"})


@login_required
def job_mine(request):
    jobs = Job.objects.filter(hr=request.user.hr_profile).order_by("-created_at")  # type: ignore
    return render(request, "jobs/job_list.html", {"jobs": jobs, "mine": True})

