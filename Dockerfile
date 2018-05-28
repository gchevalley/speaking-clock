FROM python:3-alpine
MAINTAINER Greg Chevalley <gregory.chevalley@gmail.com>

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py /usr/src/app

EXPOSE 5000

CMD [ "python", "./app.py" ]
