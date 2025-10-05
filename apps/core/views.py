from apps.core.models import Servers
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json


def home(request):
    """Home page view."""
    context = {
        'title': 'Monitoring Dashboard',
        'message': 'Welcome to the Monitoring System'
    }
    return render(request, 'core/home.html', context)

def dashboards_view(request):
    """Template view for dashboard template."""
    context = {
        'title': 'Dashboard Template',
        'message': 'Welcome to the Dashboard Template'
    }
    return render(request, 'core/dashboards.html', context)

def servers_view(request):
    """Template view for dashboard template."""
    servers = Servers.objects.all()
    context = {
        'title': 'Dashboard Template',
        'message': 'Welcome to the Dashboard Template',
        'servers': servers
    }
    return render(request, 'core/servers.html', context)

def services_view(request):
    """Template view for dashboard template."""
    
    context = {
        'title': 'Dashboard Template',
        'message': 'Welcome to the Dashboard Template',
    }
    
    return render(request, 'core/services.html', context)    

def alerts_view(request):
    """Template view for dashboard template."""
    context = {
        'title': 'Dashboard Template',
        'message': 'Welcome to the Dashboard Template'
    }
    return render(request, 'core/alerts.html', context)

def notifications_view(request):
    """Template view for dashboard template."""
    context = {
        'title': 'Dashboard Template',
        'message': 'Welcome to the Dashboard Template'
    }
    return render(request, 'core/notifications.html', context)

@csrf_exempt
@require_http_methods(["GET"])
def health_check(request):
    """Health check endpoint for monitoring."""
    return JsonResponse({
        'status': 'healthy',
        'message': 'Monitoring system is running',
        'timestamp': request.META.get('HTTP_DATE', ''),
    })
