from django.urls import path
from ticketmaster import views

urlpatterns = [
    path('ticketmaster/', views.index, name='ticketmaster-index'),
]
