from django.shortcuts import render
from .models import Magnet
# Create your views here.
from django.http import HttpResponse
# from .models import Magnet


def home(request):
    return HttpResponse('<h1>You are at the home page. Welcome World! Welcome Magnet World!</h1>')

def about(request):
    return render(request, 'about.html')

def magnets_index(request):
    magnets = Magnet.objects.all()
    return render(request, 'magnets/index.html', { 'magnets': magnets })

def magnets_detail(request, magnet_id):
    magnet = Magnet.objects.get(id=magnet_id)
    return render(request, 'magnets/detail.html', { 'magnet': magnet })

# class Magnet:
#     def __init__(self, M_id, name, kind, description, year):
#         self.id = M_id
#         self.name = name
#         self.type = kind
#         self.description = description
#         self.year = year

# magnets = [
#     Magnet('1', 'Castle', 'travel', 'Denmark', '2017'),
#     Magnet('2', 'Pizza Hut', 'food', 'pizza', '2019'),
#     Magnet('3', 'ACountants', 'business card', 'ACountants', '2021')
# ]