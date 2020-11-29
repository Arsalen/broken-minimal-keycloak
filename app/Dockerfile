FROM python:3.8-slim

LABEL maintainer="admin@yields-io" \
      application="fixed-minimal-demo" \
      release-data="2020-11-29"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . .

RUN python3 -m pip install -r requirements.txt

RUN pip install gunicorn

ENTRYPOINT ["gunicorn", "-c", "python:config.gunicorn", "app:app"]
