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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path

from index import views

urlpatterns = [
    path('index/', include('index.urls', namespace='first')),
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('test/<int:id>', views.test, name='test'),
    path('test_if/', views.test_if),
    path('test_html/', views.test_html),
    path('test01_for/', views.test01_for),
    path('test_forloop/', views.test_forloop),
    path('test_for/', views.test_for),
    path('test_url/', views.test_url),
    path('tag/', views.tag),
    path('in_tag/', views.in_tag),
    path('test_base/', views.index_html),
    path('base/', views.base_html),
    path('filter_tag/', views.filter_tag),
    path('redict/', views.redict_url),
    path('reverse/', views.test_to_reverse),
    url('test/(?P<year>[0-9]{4})/', views.year_test),
    url('test/(?P<id>[a-zA-Z0-9]+)/num/', views.num2_view),
    url('test/(?P<id>[a-zA-Z0-9]+)/num1/', views.num1_view),
    url('test/(?P<id>[a-zA-Z0-9]+)/num2/', views.num1_view),
    # re_path
    path('annotate/',views.test_annotate)
]
