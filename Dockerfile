FROM python:3.11-rc-bullseye

ENV PYTHONBUFFERED 1

WORKDIR /car_rental

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

RUN python3 manage.py makemigrations carrental
RUN python3 manage.py migrate
ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000"]