from django.db import models

# Create your models here.
class Car(models.Model):
    car_make = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    car_year = models.CharField(max_length = 50)
    car_location = models.CharField (max_length = 50)
    car_rented = models.BooleanField()

    # Overrides the default to string method to print the title, author, genre and price of a book object if print()
    # is called on an object.
    def __str__(self):
        car_string = f'{self.car_make} {self.car_model} {self.car_year} {self.car_location} rented: {self.car_rented}'
        return car_string



class Customer(models.Model):
    cus_name = models.CharField(max_length=256)
    cus_address = models.CharField(max_length=50)
    cus_age = models.CharField(max_length = 50)

    # Overrides the default to string method to print the title, author, genre and price of a book object if print()
    # is called on an object.
    def __str__(self):
        cus_string = f'{self.cus_name} {self.cus_age} {self.cus_address}'
        return cus_string



class Customer(models.Model):
    emp_name = models.CharField(max_length=256)
    emp_address = models.CharField(max_length=50)
    emp_branch = models.CharField(max_length = 50)

    # Overrides the default to string method to print the title, author, genre and price of a book object if print()
    # is called on an object.
    def __str__(self):
        emp_string = f'{self.emp_name} {self.emp_address} {self.emp_branch} '
        return emp_string

