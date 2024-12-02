from django.urls import path
from . import views

urlpatterns = [
    path('', views.map_view, name='map'),
    path('add/', views.add_event, name='add_event'),
]