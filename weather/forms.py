from django import forms



class NameForm(forms.Form):
    name = forms.CharField(max_length=50)

    widgets = {
        'name':forms.TextInput(attrs={'class':'form-control'})
    }