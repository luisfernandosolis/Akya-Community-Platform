from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

class  Login(View):
    def get(self,request):
        return render(request,"user/login.html",{})
    def post(self,request):
        username=request.POST["username"]
        password=request.POST["password"]
        print(username, password)
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            print("no ok")
            return render(request,"user/login.html",{})

@method_decorator(login_required, name='dispatch')
class Dashboard(View):
    def get(self,request):
        print(request.user.is_authenticated)
        return render(request,"user/dashboard.html",{})