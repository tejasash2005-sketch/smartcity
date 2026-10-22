from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('surveillance/', include('surveillance.urls')),
    path('alerts/', include('alerts.urls')),
    path('cameras/', include('cameras.urls')),
    path('analytics/', include('analytics.urls')),
    path('incidents/', include('incidents.urls')),
    path('reports/', include('reports.urls')),
    path('patrol/', include('patrol.urls')),
    path('evidence/', include('evidence.urls')),
    path('settings/', include('settings_app.urls')),
    path('map/', include('map.urls')),
    path('notifications/', include('notifications.urls')),
    path('audit/', include('audit.urls')),
    path('ai/', include('ai_engine.urls')),
]
