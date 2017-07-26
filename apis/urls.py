# ----- Imports ---------------------------------------------------------------
from django.conf.urls import url

from . import views

app_name = 'apis'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^yelp_search$', views.yelp_search, name='yelp_search'),
    url(r'^submit_business_name$', views.submit_business_name, name='submit_business_name'),
    url(r'^submit_phone$', views.submit_phone, name='submit_phone'),
]
