from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from .models import ItemCarrito
from productos.models import Producto

class AgregarAlCarritoView(View):
    def post(self, request, producto_id):
        producto = Producto.objects.get(id=producto_id)
        item, creado = ItemCarrito.objects.get_or_create(
            usuario=request.user,
            producto=producto
        )
        item.cantidad += 1
        item.save()
        return redirect('carrito')

