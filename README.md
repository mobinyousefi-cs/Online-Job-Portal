# Online Job Portal (Django)

A clean, production‑ready Django web app where **employers (HR)** can post jobs and manage applicants, and **job seekers** can browse and apply **without creating an account**.

> Author: **Mobin Yousefi** (GitHub: [github.com/mobinyousefi-cs](https://github.com/mobinyousefi-cs))  
> License: **MIT**

---

## ✨ Features
- **Employer (HR) authentication** with email + password
- **Job management**: create, edit, publish/unpublish, archive
- **Application intake** without login (resume upload, email notifications)
- **Search & filters**: keyword, location, experience, salary range, remote/on‑site
- **Secure file uploads** with size & type validation
- **Clean Bootstrap UI** with responsive layout
- **Admin panel** for superusers
- **CI/CD ready**: Ruff + Black + pytest on GitHub Actions
- **12‑factor** config via environment variables

---

## 🧱 Project Structure (src/ layout)
```
job-portal/
├─ LICENSE
├─ README.md
├─ pyproject.toml
├─ requirements.txt
├─ .editorconfig
├─ .gitignore
├─ .github/workflows/ci.yml
├─ Dockerfile
├─ manage.py
└─ src/
   ├─ jobportal/                # Django project package
   │  ├─ __init__.py
   │  ├─ settings.py
   │  ├─ urls.py
   │  ├─ wsgi.py
   │  └─ asgi.py
   ├─ apps/
   │  ├─ core/                  # Home, base templates, shared utils
   │  │  ├─ __init__.py
   │  │  ├─ apps.py
   │  │  ├─ urls.py
   │  │  ├─ views.py
   │  │  └─ templates/
   │  │     ├─ base.html
   │  │     └─ core/index.html
   │  ├─ accounts/              # HR auth & profile
   │  │  ├─ __init__.py
   │  │  ├─ apps.py
   │  │  ├─ models.py
   │  │  ├─ forms.py
   │  │  ├─ urls.py
   │  │  ├─ views.py
   │  │  └─ templates/accounts/
   │  │     ├─ login.html
   │  │     └─ register.html
   │  └─ jobs/                  # Jobs & Applications
   │     ├─ __init__.py
   │     ├─ apps.py
   │     ├─ models.py
   │     ├─ forms.py
   │     ├─ urls.py
   │     ├─ views.py
   │     ├─ services.py
   │     ├─ validators.py
   │     └─ templates/jobs/
   │        ├─ job_list.html
   │        ├─ job_detail.html
   │        ├─ job_form.html
   │        └─ application_submitted.html
   ├─ static/
   │  ├─ css/main.css
   │  └─ img/
   └─ tests/
      ├─ __init__.py
      ├─ test_jobs.py
      └─ test_accounts.py
```

---

## 🚀 Quickstart

### 1) Environment
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
cp .env.example .env  # (create your env values)
```

### 2) Database & static
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
```

### 3) Run
```bash
python manage.py runserver
```
Visit: http://127.0.0.1:8000

---

## 🔐 Environment Variables
Create `.env` in project root:
```
DJANGO_DEBUG=True
DJANGO_SECRET_KEY=change-me
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
DB_ENGINE=sqlite
# For Postgres example:
# DB_ENGINE=postgres
# DB_NAME=jobportal
# DB_USER=postgres
# DB_PASSWORD=postgres
# DB_HOST=localhost
# DB_PORT=5432
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
DEFAULT_FROM_EMAIL=noreply@example.com
MAX_UPLOAD_MB=5
ALLOWED_RESUME_TYPES=.pdf,.doc,.docx
```

---

## 🗄️ Data Model (high‑level)
**accounts.HRProfile**
- user (OneToOne → auth.User)
- organization_name

**jobs.Job**
- hr (FK → HRProfile)
- title, description (rich text ready), location, salary_min, salary_max, experience_years, is_remote, is_published, created_at

**jobs.Application**
- job (FK → Job)
- name, dob, gender, mobile, email, resume (FileField)
- created_at

---

## 🧪 Testing
```bash
pytest -q
```

---

## 🐳 Docker
```bash
docker build -t jobportal:latest .
docker run --env-file .env -p 8000:8000 jobportal:latest
```

---

## 📜 License
MIT — see `LICENSE`.

