from django.urls import path
from . import views

urlpatterns = [
    path('', views.tracks, name='tracks'),
    path('track/<str:pk>/', views.track, name='track'),

    path('add-track/', views.add_track, name="add-track")
]