from django.urls import path
from . import views

urlpatterns = [
    path('store3/', views.members, name='store3'),
]