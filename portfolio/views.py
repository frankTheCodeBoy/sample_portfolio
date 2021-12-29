from django.shortcuts import render, reverse
from django.http import HttpResponse

def index(request):
    return render(request, 'portfolio/index.html', {})

def about(request):
    return render(request, 'portfolio/about.html', {})

def projects(request):
    return render(request, 'portfolio/projects.html', {})

def services(request):
    return render(request, 'portfolio/services.html', {})

def contact(request):
    return render(request, 'portfolio/contact.html', {})