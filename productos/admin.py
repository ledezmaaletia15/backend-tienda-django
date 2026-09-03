from django.contrib import admin
from .models import Producto

# Para que el sitio pueda administrarlo
admin.site.register(Producto)