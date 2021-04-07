from django.contrib import admin
from .models import Material,Botella,Plastico,Papel,TipoPapel
# Register your models here.

admin.site.register(Botella)
admin.site.register(Plastico)
admin.site.register(Papel)
admin.site.register(TipoPapel)