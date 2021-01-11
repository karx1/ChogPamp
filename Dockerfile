FROM python:3.8.6-buster
COPY . /data
WORKDIR /data
RUN pip install -r requirements.txt
CMD python ./main.py