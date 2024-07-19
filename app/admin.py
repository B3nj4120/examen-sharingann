from django.contrib import admin
from .models import numero_serie, tienda, usuario, contacto

# Register your models here.
admin.site.register(numero_serie)
admin.site.register(tienda)
admin.site.register(usuario)

admin.site.register(contacto)