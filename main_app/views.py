from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# from .models import Magnet

class Magnet:
    def __init__(self, name, type, description, year):
        self.name = name
        self.type = type
        self.descripton = description
        self.year = year

magnets = [
    Magnet('Castle', 'travel', 'Denmark', '2017'),
    Magnet('Pizza Hut', 'food', 'pizza', '2019'),
    Magnet('ACountants', 'business card', 'ACountants', '2021')
]

def home(request):
    return HttpResponse('<h1>You are at the home page. Welcome World! Welcome Magnet World!</h1>')

def about(request):
    return render(request, 'about.html')

def magnets_index(request):
    # magnets = Magnet.objects.all()
    return render(request, 'cats/index.html', { 'magnets': magnets })

# def magnets_detail(request, magnet_id):
#     magnet = Magnet.objects.get(id=cat_id)
#     return render(request, 'cats/detail.html', { 'magnet': magnet })