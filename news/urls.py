__author__ = 'niels'

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.news, name='news'),
    url(r'^p/(.*)/$', views.specific_post, name='specific_post'),
    url(r'^archive/$', views.archive, name='archive'),
]
