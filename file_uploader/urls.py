from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.documents, name='documents'),
    url(r'^category/(.*)$', views.documents, name='category'),
]