from http.client import OK
from django.shortcuts import render
from django.http import HttpResponse
from carrental.models import Car, Employee, Customer
from django.shortcuts import render
from rest_framework.response import Response
from .serializers import CarSerializer, EmployeeSerializer, CustomerSerializer
from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view

#Based on lecture 8 car api examples

####################################################
# Car views

# getting a list of the cars
@api_view(['GET'])
def get_cars(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    print(serializer.data)
    return Response(serializer.data, status = status.HTTP_200_OK)

#posting a new car
@api_view(['POST'])
def save_car(request):
    serializer = CarSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

#changes an exisitng car based on vin number
@api_view(['PUT'])
def update_car(request, vin):
    try:
        theCar = Car.objects.get(car_vin = vin)
    except Car.DoesNotExists:
        return Response(status = status.HTTP_404_NOT_FOUND)
    serializer = CarSerializer(theCar, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else: 
        return Response(status = status.HTTP_400_BAD_REQUEST)


#deleting a car based on vin number
@api_view(['DELETE'])
def delete_car(request, vin):
    try:
        theCar = Car.objects.get(car_vin = vin)
    except Car.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    theCar.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

###############################################################
# Employee views

# getting a list of the employees
@api_view(['GET'])
def get_employees(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data, status = status.HTTP_200_OK)

#posting a new employee
@api_view(['POST'])
def save_employee(request):
    serializer = EmployeeSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

#changes an exisitng emplyee based on emplyee id
@api_view(['PUT'])
def update_employee(request, id):
    try:
        theEmployee = Employee.objects.get(emp_id = id)
    except Employee.DoesNotExists:
        return Response(status = status.HTTP_404_NOT_FOUND)
    serializer = EmployeeSerializer(theEmployee, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else: 
        return Response(status = status.HTTP_400_BAD_REQUEST)


#deleting an employee based on id
@api_view(['DELETE'])
def delete_employee(request, id):
    try:
        theEmployee = Employee.objects.get(emp_id = id)
    except Employee.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    theEmployee.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


################################################################
# Customer views 

# getting a list of all the customers
@api_view(['GET'])
def get_customers(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data, status = status.HTTP_200_OK)

#posting a new customer
@api_view(['POST'])
def save_customer(request):
    serializer = CustomerSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

#changes an exisitng customer based on id
@api_view(['PUT'])
def update_customer(request, id):
    try:
        theCustomer = Customer.objects.get(cus_id = id)
    except Customer.DoesNotExists:
        return Response('customer not found', status = status.HTTP_404_NOT_FOUND)
    serializer = CustomerSerializer(theCustomer, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
    else: 
        return Response(status = status.HTTP_400_BAD_REQUEST)


#deleting a customer based on id
@api_view(['DELETE'])
def delete_customer(request, id):
    try:
        theCustomer = Customer.objects.get(cus_id = id)
    except Customer.DoesNotExist:
        return Response('customer not found', status = status.HTTP_404_NOT_FOUND)
    theCustomer.delete()
    return Response('customer deleted', status=status.HTTP_202_ACCEPTED)


################################################################
# Book, Rent, Delete Booking and Return car

# A customer is linked to an order/booking for a particular car 
# We chose to implement this as a variable booked_car on the customer object that is updated with the vin number of the ordered car.

@api_view(['PUT'])
def order_car(request, id, vin):
    try:
        theCustomer = Customer.objects.get(cus_id = id)
        theCar = Car.objects.get(car_vin = vin)
    except Customer.DoesNotExist or Car.DoesNotExist:
        return Response('car or customer does not exist', status = status.HTTP_404_NOT_FOUND)

    if theCustomer.booked_car == 0 and theCar.car_status == 'available':
        theCustomer.booked_car = vin
        theCar.car_status = 'booked'

        theCustomer.save()
        theCar.save()
        return Response('car booked', status = status.HTTP_200_OK)

    return Response(status = status.HTTP_400_BAD_REQUEST)

# canceling an order/booking that a customer has made for a particular car
@api_view(['PUT'])
def cancel_order(request, id, vin):
    try:
        theCustomer = Customer.objects.get(cus_id=id)
        theCar = Car.objects.get(car_vin=vin)
    except Customer.DoesNotExist or Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    print(theCustomer.booked_car, ' ', vin, theCar.car_status)

    if theCustomer.booked_car == vin and theCar.car_status == 'booked':
        theCar.car_status = 'available'
        theCustomer.booked_car = 0

        theCar.save()
        theCustomer.save()
        return Response('order deleted', status = status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Renting a particular car a customer has ordered/booked
# We chose to implement this as a variable rented_car on the customer object that is updated with the vin number of the ordered car.
@api_view(['PUT'])
def rent_car(request, id, vin):
    try:
        theCustomer = Customer.objects.get(cus_id=id)
        theCar = Car.objects.get(car_vin=vin)
    except Customer.DoesNotExist or Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    if theCustomer.booked_car == vin and theCar.car_status == 'booked':
        theCar.car_status = 'rented'
        theCustomer.rented_car = vin
        theCustomer.booked_car = 0

        theCar.save()
        theCustomer.save()
        return Response('car rented', status = status.HTTP_202_ACCEPTED)
    else: 
        return Response('this car is not booked by this customer', status=status.HTTP_400_BAD_REQUEST)


# Returns a car a customer has rented and sets a status for it based on 
# the state of the car upon return
@api_view(['PUT'])
def return_car(request, id, vin, state):
    try:
        theCustomer = Customer.objects.get(cus_id=id)
        theCar = Car.objects.get(car_vin=vin)

    except Customer.DoesNotExist or Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # If the car is not damaged upon return it is made availale for new orders
    if theCustomer.rented_car == vin and theCar.car_status == 'rented' and state == 'ok':
        theCar.car_status = 'available'
        theCustomer.rented_car = 0
        theCar.save()
        theCustomer.save()

        return Response('car returned in good condition', status = status.HTTP_202_ACCEPTED)
    
    # If the car is damaged upon return it is made unavailable for new orders.
    elif theCustomer.rented_car == vin and theCar.car_status == 'rented' and state == 'damaged':
        theCar.car_status = 'damaged'
        theCustomer.rented_car = 0
        theCar.save()
        theCustomer.save()

        return Response('car returned in damaged condition', status = status.HTTP_202_ACCEPTED)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)