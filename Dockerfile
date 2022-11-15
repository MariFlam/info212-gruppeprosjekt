FROM python:3.11-rc-bullseye

ENV PYTHONBUFFERED 1

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY  /INFO212_oblig4/car_rental .

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]