from django.conf.urls import patterns, url
from neighbors import views

urlpatterns = patterns('neighbors.views',
    url(r'^broadcast', broadcast, name='broadcast'),
)
