from email.policy import default
from django.db import models

# A class that models a car. We have used the vin number as the identifyin feature throughout.
class Car(models.Model):
    car_vin = models.IntegerField(default=0)
    car_make = models.CharField(max_length=50, default=None)
    car_model = models.CharField(max_length=50, default=None)
    car_year = models.CharField(max_length=50, default=None)
    car_location = models.CharField(max_length=50, default=None)
    car_status = models.CharField(max_length=50, default="available")

    # Overrides the default to string method to print object details
    def __str__(self):
        car_string = f"{self.car_vin} {self.car_make} {self.car_model} {self.car_year} {self.car_location} {self.car_status}"
        return car_string

# A class hat models a customer. We have used cus_id as the identifying feature throughout

class Customer(models.Model):
    cus_id = models.IntegerField(default=0)
    cus_name = models.CharField(max_length=256)
    cus_address = models.CharField(max_length=50)
    cus_age = models.CharField(max_length=50)
    booked_car = models.IntegerField(default=0)
    rented_car = models.IntegerField(default=0)

    # Overrides the default to string method to print object details
    def __str__(self):
        cus_string = f"{self.cus_id} {self.cus_name} {self.cus_age} {self.cus_address}"
        return cus_string

# A class that models an employee. We have used emp_id as the identifying feature throughout.

class Employee(models.Model):
    emp_id = models.IntegerField(default=0)
    emp_name = models.CharField(max_length=256)
    emp_address = models.CharField(max_length=50)
    emp_branch = models.CharField(max_length=50)


    # Overrides the default to string method to print object details
    def __str__(self):
        emp_string = f"{self.emp_name} {self.emp_address} {self.emp_branch} "
        return emp_string
