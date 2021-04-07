from django.contrib import admin
from .models import Usuario,DetalleUsuario,Categoria
# Register your models here.

admin.site.register(Usuario)
admin.site.register(DetalleUsuario)
admin.site.register(Categoria)