from django import forms

color={
    "Blue" : "Blue",
    "Yellow" : "Yellow",
    "Red" : "Red",
    "Pink" : "pink",
    }   


BIRTH_YEAR_CHOICES = ["1980", "1981", "1982"]

class userform(forms.Form):
    num1 = forms.CharField(label="value_1", required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    num3 = forms.CharField()
    choose = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=color)
    