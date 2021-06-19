FROM python:3.8-slim

WORKDIR /app
ADD . /app
COPY . .

EXPOSE 5000

ENV FLASK_APP=app.py
ENV ENV_test=123 

RUN pip install -r requirement.txt

CMD [ "python","app.py" ]