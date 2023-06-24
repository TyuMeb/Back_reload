FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN rm -r nginx

RUN python manage.py collectstatic --no-input

EXPOSE 80

CMD export && python manage.py migrate && (gunicorn --log-level debug --bind 0.0.0.0:80 config.wsgi)