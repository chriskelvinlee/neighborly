from django.conf.urls import patterns, url

from neighbors import views

urlpatterns = patterns('',
    url(r'^$', 'neighbors.views.homepage', name='home'),
    url(r'^message', 'neighbors.views.messagepage', name='message')
)

