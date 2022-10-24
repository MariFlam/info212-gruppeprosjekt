from django.shortcuts import render
from django.http import HttpResponse
from carrental.models import Car

def index(request):
    return HttpResponse("Under construction. Come back tomorrow for cars")

""" car = Car.objects.all().order_by('car_model')
    context = {
        'cars': car
    }
    return render(request, 'index.html', context)"""


"""# Create your views here.
create, add, delete
crud bruke dette imetodene for å endre på de lagrede objektene og legge til nye


get, post and put changes through the api"""