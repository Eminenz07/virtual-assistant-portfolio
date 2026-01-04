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

WORKDIR /app/portfolio_cms

# --- CHANGE IS HERE: Removed collectstatic from build ---
# RUN python manage.py collectstatic --noinput

# --- AND HERE: Added it to CMD to run at startup ---
CMD ["sh", "-c", "python manage.py collectstatic --noinput && python manage.py migrate && python manage.py ensure_admin && gunicorn portfolio_cms.wsgi:application --bind 0.0.0.0:8000"]