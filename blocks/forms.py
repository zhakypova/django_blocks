from django import forms

from .models import Block, Apartment

class BlockForm(forms.ModelForm):
    class Meta:
        model = Block
        fields = '__all__'

class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = '__all__'

