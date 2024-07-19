from django.urls import path
from .views import inicio,home , carrito, contacto , login , quienessomos, registro, agregar_producto, listar_producto, modificar_producto, eliminar_producto


urlpatterns = [
    path('inicio', inicio, name="tienda"),
    path('', home, name="home"),
    path('carrito/', carrito, name="carrito"),
    path('contacto', contacto, name="contacto"),
    path('login', login, name="login"),
    path('quienessomos', quienessomos, name="quienes-somos"),
    path('registro', registro, name="registro"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-producto/', listar_producto, name="listar_producto"),
    path('modifica-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto")
]
