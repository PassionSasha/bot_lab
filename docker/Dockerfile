FROM python:3-alpine
FROM jenkins

USER root
RUN apt-get update && apt-get install bash && apt-get install -y locales && locale-gen en_US.UTF-8
RUN apt-get install -y python-pip3
RUN pip install --upgrade pip3
RUN cd /usr/local/bin && \
curl https://master.dockerproject.org/linux/amd64/docker > docker  && \
chmod +x docker  && \
groupadd -g 999 docker && \
usermod -a -G docker jenkins

WORKDIR /usr/local/bin
COPY bot1.sh ./
COPY requirements.txt ./

RUN chmod +x+r+w ./bot1.sh
RUN ./bot1.sh
RUN pip install pytelegrambot=3.7.1
WORKDIR /usr/local/bin/bot_lab
CMD [ "python", "./main.py" ]