from django.urls import path
from .views import AdminDashboard,LoginView,logoutView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', LoginView, name='login'),
    path('home/', AdminDashboard, name='home'),
    path('logout/', logoutView, name='logout'),
]
