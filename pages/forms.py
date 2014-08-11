from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    place = forms.CharField()
    length = forms.IntegerField(min_value=1, initial=1)
    #content = forms.Textarea()
