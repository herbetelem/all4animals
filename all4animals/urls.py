"""all4animals URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from alert import views
from housing import views as housing_views
from registration import views as registration_views
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('alert.urls')),
    path('', include('registration.urls')),
    
    
    path('mon_calendrier/', housing_views.my_calendar, name='mon_calendrier'),
    path('calendrier_user/', housing_views.user_calendar, name='calendrier_user'),
    path('recherche_hebergement/', housing_views.housing_search, name='recherche_hebergement'),
    path('hebergement/', housing_views.housing, name='hebergement'),

    #Lier au formulaire d'authentification django
    path('', include("django.contrib.auth.urls")),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
