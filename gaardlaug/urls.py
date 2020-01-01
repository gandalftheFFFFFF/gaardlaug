"""gaardlaug URL Configuration

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
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from news.views import latest
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', latest, name='latest'),
    url(r'^news/', include('news.urls')),
    url(r'^board/', include('board.urls')),
    url(r'^documents/', include('file_uploader.urls')),
    url(r'^affald/$', TemplateView.as_view(template_name='affald.html'), name='affald'),
    url(r'^kontakt/$', TemplateView.as_view(template_name='kontakt.html'), name='kontakt'),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
