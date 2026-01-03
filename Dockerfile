FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY portfolio_cms/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app/portfolio_cms

# Collect static files
# We run this during build so they are ready in the image
WORKDIR /app/portfolio_cms
RUN python manage.py collectstatic --noinput

# Run gunicorn
# We chain migrations here because we are using SQLite on Fly.io (no separate release VM)
CMD ["sh", "-c", "python manage.py migrate && python manage.py ensure_admin && gunicorn portfolio_cms.wsgi:application --bind 0.0.0.0:8000"]
