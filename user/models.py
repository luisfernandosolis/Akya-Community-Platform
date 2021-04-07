from django.db import models

# Create your models here.

class Categoria(models.Model):
    categoria=models.CharField(max_length=10)
    def __str__(self):
        return self.categoria
class Usuario(models.Model):
    familia=models.CharField(max_length=100)
    jefe_familia=models.CharField(max_length=50)
    internet=models.BooleanField()
    celular=models.IntegerField()
    direccion=models.CharField(max_length=100)
    cantidad_integrante=models.IntegerField()
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    def __str__(self):
        return "Los "+self.familia
class DetalleUsuario(models.Model):
    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    puntos=models.IntegerField()
    def __str__(self):
        return "{} : {} puntos".format(self.usuario,self.puntos)

