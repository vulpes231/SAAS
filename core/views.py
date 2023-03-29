from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'core/index.html')


def about(request):
    return render(request, 'core/about.html')


def services(request):
    return render(request, 'core/services.html')


def pricing(request):
    return render(request, 'core/pricing.html')

@login_required(login_url='users:login')
def profile(request):
    return render(request, 'core/profile.html')
