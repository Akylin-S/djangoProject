"""djangoProject URL Configuration

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
from django.contrib import admin
from django.urls import path

from index import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('test/', views.test),
    path('test_if/', views.test_if),
    path('test_html/', views.test_html),
    path('test01_for/', views.test01_for),
    path('test_forloop/', views.test_forloop),
    path('test_for/', views.test_for),
    path('test_url/', views.test_url, name='hello')
]
