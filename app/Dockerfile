FROM python:3.8-slim
ENV PYTHONUNBUFFERED=1
RUN mkdir /var/www
COPY requirements.txt /var/www/
RUN cd /var/www && \
    python3 -m pip install -r requirements.txt
COPY app.py .
COPY config config
RUN pip install gunicorn
ENTRYPOINT ["gunicorn", "-c", "python:config.gunicorn", "app:app"]
