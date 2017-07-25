# ----- Imports ---------------------------------------------------------------
from django.conf.urls import url

from . import views

app_name = 'apis'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^bastards$', views.nother, name='nother'),
    url(r'^yelp_search$', views.yelp_search, name='yelp_search'),
    url(r'^submit_info$', views.submit_info, name='submit_info'),
]
