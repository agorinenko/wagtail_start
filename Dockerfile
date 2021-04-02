ARG PIP_INDEX_URL
ARG PIP_TRUSTED_HOST
ARG DOCKER_REGISTRY

FROM ${DOCKER_REGISTRY}python:3.8

EXPOSE 8000

WORKDIR /opt/app
VOLUME ["/opt/app/public", "/opt/app/log"]
COPY . .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.gunicorn.txt --default-timeout=100

RUN chgrp -R 0 /opt/app/ && chmod -R g=u /opt/app/
RUN ["chmod", "+x", "/opt/app/docker-entrypoint.sh"]

ENTRYPOINT ["/opt/app/docker-entrypoint.sh"]