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

####################################################
# Car

# An index with a list of the cars in the database
"""def index(request):
    car = Car.objects.all()
    context = {
        'car_make':car,
        'car_model':car,
        'cars':car,
    }
    return render(request, 'index.html', context)"""


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
# Employee

# getting a list of the employees
@api_view(['GET'])
def get_employees(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    print(serializer.data)
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
# Customer
# getting a list of all the customers
@api_view(['GET'])
def get_customers(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    print(serializer.data)
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
        return Response(status = status.HTTP_404_NOT_FOUND)
    serializer = CustomerSerializer(theCustomer, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else: 
        return Response(status = status.HTTP_400_BAD_REQUEST)


#deleting a customer based on id
@api_view(['DELETE'])
def delete_customer(request, id):
    try:
        theCustomer = Customer.objects.get(cus_id = id)
    except Customer.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    theCustomer.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


################################################################
# Book, Rent, Delete Booking and Return car

# Book car: paramters: vin and customer id. If the customer does not have a booking and the car is available, car marked as booked

# Rent car: parameters: vin and customer id. If the customer has a booking for this car, the car status changes to rented and the customer can not rent any more cars (we need afield for this?)

# Delete booking: parameters: vin and customer id. If the customer has a booking for that car, then the car is marked as available.

# Return car: parameters: vin, customer id, car state as string ("ok", "damaged"). If the customer has rented that car and the car is "ok", the car is marked as available and the customer has no rentals registrered to them. If the customer has rented that car and the state is "damaged", then the car status is changed to damaged and the customerhas no rentals registrered to them


#https://www.django-rest-framework.org/tutorial/quickstart/


#https://www.geeksforgeeks.org/django-rest-api-crud-with-drf/

@api_view(['PUT'])
def order_car(request, id, vin):
    try:
        theCustomer = Customer.objects.get(cus_id = id)
        theCar = Car.objects.get(car_vin = vin)
    except Customer.DoesNotExist or Car.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if theCustomer.booked_car == 0 and theCar.car_status == 'available':
        theCustomer.booked_car = vin
        theCar.car_status = "booked"

        theCustomer.save()
        theCar.save()
        return Response(status = status.HTTP_200_OK)

    return Response(status = status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def cancel_order_car(request, id, vin):
    try:
        theCustomer = Customer.objects.get(cus_id=id)
        theCar = Car.objects.get(car_vin=vin)
    except Customer.DoesNotExist or Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if theCustomer.booked_car == vin and theCar.car_status == "booked":
        theCar.car_status = "available"
        theCustomer.booked_car = 0

    serializer = CustomerSerializer(theCustomer, data=request.data)
    car_serializer = CarSerializer(theCar, data=request.data)
    if serializer.is_valid() and car_serializer.is_valid():
        serializer.save()
        car_serializer.save()
        return Response(serializer.data, car_serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def rent_car(request, id, vin):
    try:
        theCustomer = Customer.objects.get(cus_id=id)
        theCar = Car.objects.get(car_vin=vin)
    except Customer.DoesNotExist or Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    if theCustomer.booked_car == vin and theCar.car_status == "booked":
        theCar.car_status = "rented"
        theCustomer.rented_car = vin
        theCustomer.booked_car = 0

    serializer = CustomerSerializer(theCustomer, data=request.data)
    car_serializer = CarSerializer(theCar, data=request.data)
    if serializer.is_valid() and car_serializer.is_valid():
        serializer.save()
        car_serializer.save()
        return Response(serializer.data, car_serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def return_car(request, id, vin, state):
    try:
        theCustomer = Customer.objects.get(cus_id=id)
        theCar = Car.objects.get(car_vin=vin)
    except Customer.DoesNotExist or Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if theCustomer.rented_car == vin and theCar.car_status == "rented" and state == "ok":
        theCar.car_status = "available"
        theCustomer.rented_car = 0

    elif theCustomer.rented_car == vin and theCar.car_status == "rented" and state == "damaged":
        theCar.car_status = "damaged"
        theCustomer.rented_car = 0

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
        

    serializer = CustomerSerializer(theCustomer, data=request.data)
    car_serializer = CarSerializer(theCar, data=request.data)
    if serializer.is_valid() and car_serializer.is_valid():
        serializer.save()
        car_serializer.save()
        return Response(serializer.data, car_serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)