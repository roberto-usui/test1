FROM ubuntu:20.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
RUN apt-get install -y build-essential libpq-dev
RUN pip3 install -r requirements.txt
COPY . /app
RUN python3 manage.py recreate_db && python3 manage.py setup_dev

EXPOSE 5000

CMD ["gunicorn", "-b 0.0.0.0:5000", "run:app"]
