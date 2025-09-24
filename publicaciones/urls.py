from django.urls import path
from .views import ProductosEnVentaView
from .views import ProductoDetalleView

urlpatterns = [
    path('', ProductosEnVentaView.as_view(), name='productos_en_venta'),
    path('producto/<int:pk>/', ProductoDetalleView.as_view(), name='producto_detalle'),
]