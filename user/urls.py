from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
appname="user"
urlpatterns = [
    path('login/', views.Login.as_view(),name="login"),
    path('dashboard/', views.Dashboard.as_view(),name="dashboard"),
    path("/logout",LogoutView.as_view(),name="logout")

]