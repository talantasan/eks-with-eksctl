# syntax=docker/dockerfile:1

FROM python:3.14.0a1-bullseye

WORKDIR /python-docker
ENV FLASK_APP=myapp1.py
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
CMD ["flask", "run", "--host=0.0.0.0"]