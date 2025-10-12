from apps.core.models import Servers
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

# added for authentication
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

import json


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('core:home')  # redirect after successful login
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'core/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='core:login')
def home(request):
    """Home page view."""
    context = {
        'title': 'Monitoring Dashboard',
        'message': 'Welcome to the Monitoring System'
    }
    return render(request, 'core/home.html', context)

@login_required(login_url='core:login')
def dashboards_view(request):
    """Template view for dashboard template."""
    context = {
        'title': 'Dashboard Template',
        'message': 'Welcome to the Dashboard Template'
    }
    return render(request, 'core/dashboards.html', context)

@login_required(login_url='core:login')
def servers_view(request):
    """Template view for dashboard template."""
    servers = Servers.objects.all()
    context = {
        'title': 'Dashboard Template',
        'message': 'Welcome to the Dashboard Template',
        'servers': servers
    }
    return render(request, 'core/servers.html', context)

@login_required(login_url='core:login')
def services_view(request):
    """Template view for dashboard template."""
    
    context = {
        'title': 'Dashboard Template',
        'message': 'Welcome to the Dashboard Template',
    }
    
    return render(request, 'core/services.html', context)    

@login_required(login_url='core:login')
def alerts_view(request):
    """Template view for dashboard template."""
    context = {
        'title': 'Dashboard Template',
        'message': 'Welcome to the Dashboard Template'
    }
    return render(request, 'core/alerts.html', context)

@login_required(login_url='core:login')
def notifications_view(request):
    """Template view for dashboard template."""
    context = {
        'title': 'Dashboard Template',
        'message': 'Welcome to the Dashboard Template'
    }
    return render(request, 'core/notifications.html', context)

@login_required(login_url='core:login')
def settings_view(request):
    """Template view for dashboard template."""
    context = {
        'title': 'Dashboard Template',
        'message': 'Welcome to the Dashboard Template'
    }
    return render(request, 'core/settings.html', context)

@csrf_exempt
@require_http_methods(["GET"])
def health_check(request):
    """Health check endpoint for monitoring."""
    return JsonResponse({
        'status': 'healthy',
        'message': 'Monitoring system is running',
        'timestamp': request.META.get('HTTP_DATE', ''),
    })
