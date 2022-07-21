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
    path('purposes/', views.PurposeList.as_view(), name='purpose_index'),
    path('purposes/<int:magnet_id>', views.PurposeDetail.as_view(), name='purpose_detail'),
    path('purposes/create', views.PurposeCreate.as_view(), name='purposes_create'),
    path('purposes/<int:pk>/update', views.PurposeUpdate.as_view(), name='purposes_update'),
    path('purposes/<int:pk>/delete', views.PurposeDelete.as_view(), name='purposes_delete'),
    # associate a purpose with magnet (M:M)
    path('magnets/<int:magnet_id>/assoc_purpose/', views.assoc_purpose, name='assoc_purpose'),
]