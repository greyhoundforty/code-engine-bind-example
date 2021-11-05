FROM python:3.9-slim-buster

LABEL maintainer="rtiffany@us.ibm.com"

COPY . /opt

WORKDIR /opt 

RUN apt-get update && \
    apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt --user

COPY docker-entrypoint.sh /usr/local/bin

RUN chmod +x /usr/local/bin/docker-entrypoint.sh

ENTRYPOINT ["docker-entrypoint.sh"]