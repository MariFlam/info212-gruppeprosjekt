Folders: 
- Main folder: INFO212_oblig4
  - site: car_rental
  - App: carrental

Github: https://github.com/MariFlam/info212-gruppeprosjekt

Dockerhub: https://hub.docker.com/r/mfl049/django-docker

DB superuser: 
  - username: admin
  - pwd: teatime_doubly_so

Postman Cluster: https://app.getpostman.com/join-team?invite_code=5dee978ddd33fdfdb273404405f4e569&target_code=14e3ff59731237dc2d29e3f3ac1efa6a

Pipenv: 
Install (make sure you are in the main folder): 
pipenv install

run: 
pipenv shell

Packages we installed: 
- Django
- Django rest framework
- Django import/export (for easier db management. It allows you to upload JSON or csv files to populate the database. The files we used were cars.json and Customer.json)

We used the examples from lecture 8 as a starting point for how to build the apis and set up the models, urls and serializers. Some of the structure and the names of some of the variables were kept because they made sense to us.
We used the documentation for django, django import/export and django rest framework as additional references.