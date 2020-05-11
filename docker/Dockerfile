FROM python:buster
FROM jenkins

USER root
RUN apt-get update && apt-get install bash && apt-get install -y locales && locale-gen en_US.UTF-8

RUN cd /usr/local/bin && \
curl https://master.dockerproject.org/linux/amd64/docker > docker  && \
chmod +x docker  && \
groupadd -g 999 docker && \
usermod -a -G docker jenkins


WORKDIR /usr/local/bin
COPY bot1.sh ./
RUN chmod +x+r+w ./bot1.sh
RUN ./bot1.sh

WORKDIR /usr/local/bin/bot_lab
CMD [ "python", "./main.py" ]