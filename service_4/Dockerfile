FROM python:3.7

RUN apt update
RUN apt install python3-pip -y

COPY ./requierments.txt .
RUN pip install -r requierments.txt

COPY . .

EXPOSE 5003

ENTRYPOINT ["gunicorn", "--workers=2", "-b", "0.0.0.0:5003", "missiongen:app"]