from django.shortcuts import render
from django.views import generic

from .models import customer


class Customer_Create(generic.CreateView):
    model=customer
    fields=['name', 'Street_address', 'Litres', 'phone']