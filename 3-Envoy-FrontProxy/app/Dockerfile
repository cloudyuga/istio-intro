FROM python:3.7
MAINTAINER Sumit Murari "sumit@cloudyuga.guru"
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT ["python"]
CMD ["app.py"]
