FROM alpine:3.16

RUN apk add --update py3-pip

WORKDIR /app/

COPY . /app/

RUN pip install -r /app/requirements.txt

COPY crontab /var/spool/cron/crontabs/root

RUN chmod +x /app/app.py

CMD crond -l 2 -f