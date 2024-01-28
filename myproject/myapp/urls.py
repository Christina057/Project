from django.urls import path
from .views import hello_world, greet

urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('greet/', greet, name='greet'),
]
