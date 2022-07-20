from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('magnets/', views.magnets_index, name='index'),
    path('magnets/<int:magnet_id>', views.magnets_detail, name='detail'),
    path('magnets/create', views.MagnetCreate.as_view(), name='magnets_create'),
    path('magnets/<int:pk>/update', views.MagnetUpdate.as_view(), name='magnets_update'),
    path('magnets/<int:pk>/delete', views.MagnetDelete.as_view(), name='magnets_delete'),
    path('magnets/<int:magnet_id>/add_surface', views.add_surface, name='add_surface'),
]