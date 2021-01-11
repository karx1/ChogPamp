FROM python:3.8.6-buster
COPY . /data
WORKDIR /data
RUN  install -r requirements.txt
CMD python ./main.py