from django.contrib import admin

from ecommerce.models import Producto, Categoria

# Register your models here.
admin.site.register(Producto)
admin.site.register(Categoria)
