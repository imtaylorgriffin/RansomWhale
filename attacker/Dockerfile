FROM python:3.7-alpine3.15

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python

RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools



WORKDIR /home/attacker
COPY ./send.sh /home/attacker/email/send.sh
COPY ./listener.py /home/attacker/



# Creates a non-root user with an explicit UID and adds permission to access the /app folder

RUN adduser -u 5678 --disabled-password --gecos "" attacker && chown -R attacker /home/attacker/
USER attacker

#6/9 update vvvvvvvv
COPY ./attacker_files/* /home/attacker/
######################

CMD ["/bin/sh"]