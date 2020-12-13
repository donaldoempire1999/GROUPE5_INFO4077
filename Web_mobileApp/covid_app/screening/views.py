from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views import View
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required


# Create your views here.
# home
def index(request):
    return render(request, 'pages/index/index.html')


# home_office
def index_back_office(request):
    return render(request, 'pages/backOffice/index.html')


# tables des citoyens dejà depisté
def tables(request):
    return render(request, 'pages/backOffice/tables.html')


def forgot_password(request):
    return render(request, 'pages/backOffice/forgot-password.html')


def register(request):
    return render(request, 'pages/backOffice/register.html')


class LoginView(views.LoginView):
    template_name = "pages/backOffice/login.html"
    redirect_field_name = "/home"


def save_citizens(request):
    return render(request, 'pages/backOffice/save_citizens.html')
