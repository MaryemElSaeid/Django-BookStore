from django import forms 
from .models import Booklet

class BookletForm(forms.ModelForm):
    class Meta:
        model = Booklet
        fields = "__all__"