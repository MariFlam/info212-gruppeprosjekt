"""car_rental URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
import carrental.views as view

urlpatterns = [
    # car paths
    #if we want a different front-page:
    #path('', view.index, name = 'main'),
    path('admin/', admin.site.urls, name = 'admin'),
    path('get_cars/', view.get_cars, name = 'Get all the cars'),
    path('save_car/', view.save_car, name = 'Add a new car'),
    path('update_car/<int:vin>', view.update_car, name = 'Change existing car'),
    path('delete_car/<int:vin>', view.delete_car, name = 'Delete Car'),
    #customer paths
    
    path('get_customers/', view.get_customers, name = 'Get all the customers'),
    path('save_customer/', view.save_customer, name = 'Add a new customer'),
    path('update_customer/<int:id>', view.update_customer, name = 'Change existing customer'),
    path('delete_customer/<int:id>', view.delete_customer, name = 'Delete Customer'),
    # employee paths
    
    path('get_employees/', view.get_employees, name = 'Get all the employees'),
    path('save_employee/', view.save_employee, name = 'Add a new employee'),
    path('update_employee/<int:id>', view.update_employee, name = 'Change existing employee'),
    path('delete_employee/<int:id>', view.delete_employee, name = 'Delete employee'),
    #order, Rent, Delete Booking, Return car paths
    path('order_car/<int:id>/<int:vin>', view.order_car, name= 'Order car'),

    ]



#https://docs.djangoproject.com/en/4.1/intro/tutorial01/