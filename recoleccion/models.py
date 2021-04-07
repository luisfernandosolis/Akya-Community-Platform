from django.db import models
from user.models import Usuario
# Create your models here.

class Material(models.Model):
    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    peso=models.FloatField()
    precio=models.FloatField()
    class Meta:
        abstract = True




class Botella(Material):
    tapa=models.BooleanField()
    def __str__(self):
        return self.usuario.familia + " : "+str(self.peso) +" kg"

class TipoPapel(models.Model):
    tipo=models.CharField(max_length=20)
    def __str__(self):
        return self.tipo

class Papel(Material):
    tipo=models.ForeignKey(TipoPapel, on_delete=models.CASCADE)
    def __str__(self):
        return self.usuario.familia + " : "+str(self.peso) +" kg"

class Plastico(Material):
    pass
    def __str__(self):
        return self.usuario.familia + " : "+str(self.peso) +" kg"

class Lata(Material):
    pass
    def __str__(self):
        return self.usuario.familia + " : "+str(self.peso) +" kg"

