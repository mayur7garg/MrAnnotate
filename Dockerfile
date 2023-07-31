FROM python:3.11

WORKDIR /src

RUN apt-get update
RUN pip install --upgrade pip

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD /bin/bash