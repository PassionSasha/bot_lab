FROM python:buster
RUN apt-get update && apt-get install bash
RUN pip3 install pytelegrambotapi
RUN curl -fsSLO https://get.docker.com/builds/Linux/x86_64/docker-17.04.0-ce.tgz \
  && tar xzvf docker-17.04.0-ce.tgz \
  && mv docker/docker /usr/local/bin \
  && rm -r docker docker-17.04.0-ce.tgz
WORKDIR /usr/src/app
COPY bot1.sh ./
RUN chmod +x+r+w ./bot1.sh
RUN ./bot1.sh

WORKDIR /usr/src/app/bot_lab
CMD [ "python", "./main.py" ]