from django.urls import path
from . import views

urlpatterns = [
    path('store1/', views.members, name='store1'),
]