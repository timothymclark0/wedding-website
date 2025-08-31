import django.forms as forms

class ClaimForm(forms.Form):
    #full_partial = forms.CharField(label = 'full-partial')
    name = forms.CharField(label="name", max_length=255)
    amount = forms.FloatField(max_value = 10000.0,min_value=0.0,required=False, label="amount")
