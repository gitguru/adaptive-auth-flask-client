FROM python:3.11-slim-buster

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

RUN flask --app flaskr init-db
# CMD ["flask", "--app", "flaskr", "run", "--host=0.0.0.0", "--debug"]
