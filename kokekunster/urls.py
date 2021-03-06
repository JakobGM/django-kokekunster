"""kokekunster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
import os

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
    url(r'^exams/', include('examiner.urls', namespace='examiner')),
    url(
        r'^api/exams/',
        include('examiner.urls', namespace='examiner'),
        {'api': True},
    ),
    url(r'^', include('semesterpage.urls')),
]

if not os.environ.get('PRODUCTION', False):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
