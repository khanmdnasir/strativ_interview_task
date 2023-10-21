FROM python:3.11-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN pip install --upgrade pip
COPY . .
RUN pip install -r requirements.txt
# RUN python manage.py collectstatic --no-input
# RUN python manage.py makemigrations
RUN python manage.py migrate

