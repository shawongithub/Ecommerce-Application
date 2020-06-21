from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from App_Shop.models import  Product

class Home(ListView):
    model=Product
    template_name='App_Shop/home.html'

class ProductDetail(LoginRequiredMixin, DetailView):
    model=Product
    template_name='App_Shop/product_detail.html'