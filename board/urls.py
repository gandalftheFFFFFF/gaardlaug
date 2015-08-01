__author__ = 'niels'

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='board'),
]
