from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=20)
    address = forms.CharField()
    did_send  = forms.BooleanField()
