from django.urls import path
from . import views

appname="user"
urlpatterns = [
    path('', views.Main.as_view(),name="main"),


]