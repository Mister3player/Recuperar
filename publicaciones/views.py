from django.views.generic import ListView, DetailView
from .models import Producto

class ProductosEnVentaView(ListView):
    model = Producto
    template_name = 'marketplace/listado.html'
    context_object_name = 'productos'

    def get_queryset(self):
        return Producto.objects.filter(disponible=True).order_by('-fecha_publicacion')

class ProductoDetalleView(DetailView):
    model = Producto
    template_name = 'marketplace/detalle.html'
    context_object_name = 'producto'