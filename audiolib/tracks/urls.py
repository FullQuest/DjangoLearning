from django.urls import path
from . import views

urlpatterns = [
    path('', views.tracks, name='tracks'),
    path('track/<str:pk>/', views.track, name='track'),
]