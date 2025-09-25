from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Producto

class ListaProductosView(ListView):
    model = Producto
    template_name = 'productos/lista.html'

class DetalleProductoView(DetailView):
    model = Producto
    template_name = 'productos/detalle.html'
