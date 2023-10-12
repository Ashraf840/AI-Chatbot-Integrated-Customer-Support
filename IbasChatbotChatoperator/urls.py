"""IbasChatbotChatoperator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import View
from django.contrib.admin.forms import AdminAuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


urlpatterns = [
    path("admin/", admin.site.urls, name='adminURL'),
    path("", include(('home.urls', 'app_name'), namespace="homeApplication")),
    path("auth/", include(('authenticationApp.urls.urls', 'app_name'), namespace="authenticationApplication")),
    path("staff/", include(('staffApp.urls.urls', 'app_name'), namespace="staffApplication")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



admin.site.index_title = "Integrated Budget & Accounting System"
admin.site.site_header = "iBAS++ Administration"
admin.site.site_title = "iBAS++ Administration"