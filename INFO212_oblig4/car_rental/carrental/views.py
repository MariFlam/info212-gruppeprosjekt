from django.shortcuts import render
from django.http import HttpResponse
from carrental.models import Car

def cars(request):
    car = Car.objects.all().order_by('title')
    context = {
        'cars': car
    }
    return render(request, 'car_list.html', context)


"""# Create your views here.
create, add, delete
crud bruke dette imetodene for å endre på de lagrede objektene og legge til nye


get, post and put changes through the api"""