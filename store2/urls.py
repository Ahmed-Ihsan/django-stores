from django.urls import path
from . import views

urlpatterns = [
    path('store2/', views.members, name='store2'),
]