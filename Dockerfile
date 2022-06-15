FROM python:3.7-alpine3.15

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python

## Docker fails to install cffi - https://stackoverflow.com/questions/71372066/docker-fails-to-install-cffi-with-python3-9-alpine-in-dockerfile
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev \
    && apk add libffi-dev

RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

## setup.py saying invalid command 'bdist_wheel' - https://stackoverflow.com/questions/34819221/why-is-python-setup-py-saying-invalid-command-bdist-wheel-on-travis-ci
RUN pip install wheel

## required things
RUN pip install fernet
RUN pip install cryptography


WORKDIR /app
COPY ./python-files /app
COPY ./misc-files /home/appuser
COPY --from=tkotosz/mhsendmail:0.2.0 /usr/bin/mhsendmail /usr/local/bin/

# Creates a non-root user with an explicit UID and adds permission to access the /app folder

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app 
USER appuser

CMD ["/bin/sh"]