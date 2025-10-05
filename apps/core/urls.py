from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboards/', views.dashboards_view, name='dashboards'),
    path('servers/', views.servers_view, name='servers'),
    path('services/', views.services_view, name='services'),
    path('alerts/', views.alerts_view, name='alerts'),
    path('notifications/', views.notifications_view, name='notifications'),
    path('api/health/', views.health_check, name='health_check'),
]