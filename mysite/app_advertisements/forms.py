from django import forms


class AdvertisementForm(forms.Form):
    main_attrs = {'class': 'form-control-lg'}

    title =       forms.CharField(max_length=60, widget=forms.TextInput(attrs=main_attrs))
    description = forms.CharField(widget=forms.Textarea(attrs=main_attrs))
    price =       forms.DecimalField(widget=forms.NumberInput(attrs=main_attrs))
    is_auction =  forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs=main_attrs))
    image =       forms.ImageField(widget=forms.FileInput(attrs=main_attrs))

