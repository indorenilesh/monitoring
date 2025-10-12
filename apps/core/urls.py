from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboards/', views.dashboards_view, name='dashboards'),
    path('servers/', views.servers_view, name='servers'),
    path('services/', views.services_view, name='services'),
    path('alerts/', views.alerts_view, name='alerts'),
    path('notifications/', views.notifications_view, name='notifications'),
    path('settings/', views.settings_view, name='settings'),
    path('api/health/', views.health_check, name='health_check'),
        path(
        'password_change/',
        auth_views.PasswordChangeView.as_view(
            template_name='core/password_change.html',   # create this template
            success_url='/dashboards/'                   # redirect after successful change
        ),
        name='password_change'
    ),
]