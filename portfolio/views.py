from django.shortcuts import render

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

def api_project(request):
    return render(request, 'portfolio/api-project.html', {})

def book_app(request):
    return render(request, 'portfolio/book-app.html', {})

def learning_log(request):
    return render(request, 'portfolio/learning-log.html', {})

def android_project(request):
    return render(request, 'portfolio/android.html', {})

def social_site(request):
    return render(request, 'portfolio/social-network.html', {})

def game_dev(request):
    return render(request, 'portfolio/game-dev.html', {})

def global_data(request):
    return render(request, 'portfolio/global-datasets.html', {})

def machine_analytics(request):
    return render(request, 'portfolio/machine-analytics.html', {})