FROM python:buster
RUN apt-get update && apt-get install bash
RUN pip3 install pytelegrambotapi
WORKDIR /usr/src/app
COPY bot1.sh ./
RUN chmod +x+r+w ./bot1.sh
RUN ./bot1.sh

WORKDIR /usr/src/app/bot_lab
CMD [ "python", "./main.py" ]