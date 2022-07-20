from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Magnet
from .forms import SurfaceForm

# Create your views here.
def home(request):
    return HttpResponse('<h1>You are at the home page. Welcome World! Welcome Magnet World!</h1>')

def about(request):
    return render(request, 'about.html')

def magnets_index(request):
    magnets = Magnet.objects.all()
    return render(request, 'magnets/index.html', { 'magnets': magnets })

def magnets_detail(request, magnet_id):
    magnet = Magnet.objects.get(id=magnet_id)
    return render(request, 'magnets/detail.html', { 'magnet': magnet, 'surface_form': SurfaceForm() })

class MagnetCreate(CreateView):
    model =  Magnet
    fields = '__all__'
    success_url = '/magnets/'

class MagnetUpdate(UpdateView):
    model =  Magnet
    fields = ['name', 'description']

class MagnetDelete(DeleteView):
    model =  Magnet
    success_url = '/magnets/'

def add_surface(request, magnet_id):
    form = SurfaceForm(request.POST)
    if form.is_valid():
        new_surface = form.save(commit=False)
        new_surface.magnet_id = magnet_id
        new_surface.save()
        return redirect('detail', magnet_id=magnet_id)
   
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