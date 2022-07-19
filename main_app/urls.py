from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('magnets/', views.magnets_index, name='index'),
    path('magnets/<int:magnet_id>', views.magnets_detail, name='detail')
    path('magnets/create', views.magnets_index, name='index'),
    path('magnets/<int:magnet_id>', views.magnets_detail, name='detail')
    path('magnets/<int:magnet_id>', views.magnets_detail, name='detail')
]