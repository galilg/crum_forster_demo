# ----- Imports ---------------------------------------------------------------

from django.db import models

# ----- Main ------------------------------------------------------------------

class Businesses(models.Model):
    name = models.CharField(max_length=35, null=False)
    street = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=45, null=False)
    state = models.CharField(max_length=2, null=False)
    zip_code = models.IntegerField(null=False)
    google_place_id = models.CharField(max_length=100, null=True)
    yelp_id = models.CharField(max_length=45, null=True)
    yelp_rating = models.FloatField(max_length=4, null=True)
    yelp_price_level = models.CharField(max_length=5, null=True)
    yelp_no_of_reviews = models.IntegerField(null=True)
    latitude = models.FloatField(max_length=25, null=True)
    longitude = models.FloatField(max_length=25, null=True)
    phone = models.CharField(max_length=14, null=True)

    def __str__(self):
        return self.businesses_text


    def has_high_yelp_rating(self):
        if self.yelp_rating >= 4.0:
            return True
        else:
            return False
