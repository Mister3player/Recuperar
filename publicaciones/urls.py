from django.urls import path
from .views import ProductosEnVentaView, ProductoDetalleView
#
from django.contrib import admin
from django.urls import path, include
# ... (otras importaciones)

urlpatterns = [
    # ASEGÚRATE DE QUE ESTA LÍNEA ESTÉ PRESENTE    
    path('', ProductosEnVentaView.as_view(), name='productos_en_venta'),
    path('producto/<int:pk>/', ProductoDetalleView.as_view(), name='producto_detalle'),
]
# ... (el resto del archivo)
