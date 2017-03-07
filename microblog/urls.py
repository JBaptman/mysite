from django.conf.urls import url

from . import views

#Definition of the urls with the views we created
urlpatterns = [
    url(r'^$', views.home),
    url(r'^create_post/$', views.create_post),
    url(r'^delete_post/$', views.delete_post),
]