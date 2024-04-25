from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView, PasswordResetConfirmView
from django.contrib.auth import logout
# Create your views here.

from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello World!")

