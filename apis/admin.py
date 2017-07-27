
from django.contrib import admin

# Register your models here.

from .models import Businesses

class BusinessAdmin(admin.ModelAdmin):
    fields = [ 'name',
               'street',
               'city',
               'state',
               'zip_code',
               'yelp_id',
               'yelp_rating',
               'yelp_price_level',
               'latitude',
               'longitude',
               'phone']

admin.site.register(Businesses, BusinessAdmin)
