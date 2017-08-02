from python:2.7.13-alpine3.6

RUN pip install flask
COPY . /app
WORKDIR /app
EXPOSE 5000

CMD python app.py
