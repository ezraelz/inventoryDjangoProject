from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from .serializers import UserSerializer
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .form import LoginForm

@login_required
def AdminDashboard(request):
    return render(request, 'home.html', {})

def LoginView(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            # Authenticate the user
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)  # Log the user in
                return redirect('home')
            else:
                return render(request, 'login.html',{'form':form})
    return render(request, 'login.html', {'form':form})
    

def logoutView(request):
    logout(request)  # Log the user out
    return redirect('login')