from rest_framework import serializers
from .models import Car, Employee, Customer

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            'car_vin', 
            'car_make', 
            'car_model', 
            'car_year', 
            'car_location', 
            'car_status']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
           'cus_id',
           'cus_name',
           'cus_address',
           'cus_age',
           'booked_car',
           'rented_car'
        ]

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Employee
        fields = [
            'emp_id',
            'emp_name',
            'emp_address', 
            'emp_branch'
        ]
