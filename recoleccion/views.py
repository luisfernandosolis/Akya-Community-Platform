from django.shortcuts import render
from django.views import View
from user.models import Usuario,DetalleUsuario
from recoleccion.models import Botella,Plastico,Papel
# Create your views here.
class Main(View):
    def get(self,request):
        usuarios=Usuario.objects.all()
        detalles=DetalleUsuario.objects.all()
        botellas = Botella.objects.all()
        plasticos = Plastico.objects.all()
        papeles = Papel.objects.all()


        recolectores_rango={}
        recolectores = {}

        posicion=3
        for i in usuarios:
            detalles_user={}
            detalles_user["puntos"] = detalles.get(usuario=i.id).puntos
            detalles_user["botella"]=botellas.get(usuario=i.id).peso
            detalles_user["plastico"] = plasticos.get(usuario=i.id).peso
            detalles_user["papel"] = papeles.get(usuario=i.id).peso


            if i.categoria.categoria=="Plata" or i.categoria.categoria=="Oro" or i.categoria.categoria=="Bronce":
                detalles_user["familia"] = i.familia
                recolectores_rango[i.categoria.categoria] = detalles_user
            else:
                detalles_user["categoria"] = i.categoria.categoria
                detalles_user["posicion"] = posicion
                recolectores[i.familia] = detalles_user
                posicion+=1
        print(recolectores)
        return render(request, "recoleccion/index.html",context={"rango":recolectores_rango,"recolectores": recolectores})