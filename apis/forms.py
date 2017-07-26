from django import forms

class NameForm(forms.Form):
    business_name = forms.CharField(label='Business Name', max_length=35)
    city = forms.CharField(label='City', max_length=35)
    state = forms.CharField(label='State', max_length=2)

class NumberForm(forms.Form):
    phone = forms.CharField(label='Phone', max_length=20)


class LatLongForm(forms.Form):
    business_name = forms.CharField(label="Business Name", max_length=35)
    latitude = forms.FloatField(label='Latitude')
    longitede = forms.FloatField(label='Longitude')
