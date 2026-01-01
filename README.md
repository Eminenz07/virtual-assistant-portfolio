# Portfolio CMS

A Django-based Content Management System (CMS) for your portfolio website.

## Features

- **Admin Dashboard**: Manage Services, Testimonials, Experience, Skills, Certifications, Projects, and Blogs.
- **API**: serve content dynamically to your frontend.
- **Authentication**: Secure login/logout for site owner.
- **Image Handling**: Upload and manage images.

## Setup Instructions

### 1. Prerequisites

- Python 3.8+
- pip (Python package manager)

### 2. Backend Setup

1. Navigate to the `portfolio_cms` directory:

   ```sh
   cd portfolio_cms
   ```

2. Create a virtual environment (optional but recommended):

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser (for admin access):

   ```sh
   python manage.py createsuperuser
   ```

6. Run the server:
   ```sh
   python manage.py runserver
   ```
   The backend will start at `http://127.0.0.1:8000`.

### 3. Frontend Integration

The frontend `index.html` has been updated to fetch data from the API.
ensure that `assets/js/api.js` is included in your `index.html` (at the bottom of existing scripts):

```html
<script src="./assets/js/api.js"></script>
```

### 4. Deployment

#### Backend (Render.com / Railway)

1. Push `portfolio_cms` code to GitHub.
2. Connect repository to Render/Railway.
3. Set Environment Variables:
   - `DJANGO_SECRET_KEY`: (Generate a secure key)
   - `DEBUG`: `False`
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `gunicorn portfolio_cms.wsgi:application`

#### Frontend (Netlify / Vercel)

1. Push your static files (`index.html`, `assets/`) to a separate repo or folder.
2. Deploy as a static site.
3. Update `assets/js/api.js`:
   Change `const API_BASE_URL` to your production backend URL (e.g., `https://my-portfolio-cms.onrender.com/api`).

## APIs

- `/api/whatido/`
- `/api/testimonials/`
- `/api/experience/`
- `/api/skills/`
- `/api/certifications/`
- `/api/projects/`
- `/api/blogs/`

## Dashboard

Access the CMS dashboard at: `http://localhost:8000/dashboard/`
Login with your superuser credentials.
