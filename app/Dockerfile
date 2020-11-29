FROM python:3.8-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . .
RUN python3 -m pip install -r requirements.txt
RUN pip install gunicorn
ENTRYPOINT ["gunicorn", "-c", "python:config.gunicorn", "app:app"]
