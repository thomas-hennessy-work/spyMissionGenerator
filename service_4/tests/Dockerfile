FROM python:3.7

WORKDIR /testDir

RUN apt update
RUN apt install python3-pip -y

COPY ./requierments.txt .

RUN pip install -r requierments.txt

COPY . .