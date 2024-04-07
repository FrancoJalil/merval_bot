FROM alpine:latest

RUN apk add --update py3-pip

WORKDIR /app/

COPY . /app/

COPY crontab /var/spool/cron/crontabs/root

RUN chmod +x /app/app.py

CMD crond -l 2 -f