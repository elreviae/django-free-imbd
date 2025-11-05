# Django Free IMBD

[![Django 5.2](https://img.shields.io/badge/Django-5.2-green)](https://www.djangoproject.com/)
[![Bootstrap 5.3.8](https://img.shields.io/badge/Bootstrap-5.3.8-blue)](https://getbootstrap.com/)
[![Vercel](https://img.shields.io/badge/Vercel-Deployed-black)](https://vercel.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **A simple, modern Django app to explore movies and TV shows using the free [imdbapi.dev](https://imdbapi.dev/) API**

---

## Live Demo

**[https://django-free-imbd.vercel.app](https://django-free-imbd.vercel.app)**

---

## Features

- Display **upcoming movies** (current year + next year)
- Show **popular TV series** (US & UK)
- Responsive design with **Bootstrap 5.3.8**
- Posters, ratings, genres
- **Serverless deployment** on **Vercel**
- No API key required

---

## API Used – [imdbapi.dev](https://imdbapi.dev/)

> **100% free** API – 1,000 requests/day – perfect for learning and small projects.

### Endpoints Used

| Page                            | Endpoint |
|---------------------------------|---------|
| **First 50 Movies (popular)**   | `https://api.imdbapi.dev/titles?types=MOVIE&startYear={{ current_year }}&endYear={{ next_year }}&sortBy=SORT_BY_POPULARITY` |
| **First 50 TV Shows (popular)** | `https://api.imdbapi.dev/titles?types=TV_SERIES&countryCodes=US&countryCodes=GB&sortBy=SORT_BY_POPULARITY&endYear={{ current_year }}` |

## Custom var to manage date
```python
current_date = date.today()

current_year = current_date.strftime("%Y")

next_year = str(int(current_year) + 1)
```
---

## Tech Stack

| Technology | Version |
|------------|--------|
| Python | 3.11+ |
| Django | 5.2 |
| Bootstrap | 5.3.8 |
| Hosting | Vercel (Serverless) |
| API | [imdbapi.dev](https://imdbapi.dev/) |

---

## Local Setup

```bash
# 1. Clone the repo
git clone https://github.com/elreviae/django-free-imbd.git
cd django-free-imbd

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the server
python manage.py runserver

```
---
## Django Vercel Deployment Template 
- Special thanks to shellchett for his work : [@shellchett](https://github.com/shellchett/django-vercel-deployment-template)

---