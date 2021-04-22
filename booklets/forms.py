from django import forms
from .models import Booklet,Category
from django.core.exceptions import ValidationError
 
class BookletForm (forms.ModelForm):
    class Meta:
        model= Booklet
        fields= "__all__"
        exclude=("isbn","summary")

 
    def clean_title(self):
        title=self.cleaned_data.get("title")
        if len(title)>=10 and len(title)<=50:
            return title
        raise ValidationError("title must be between 10 and 50 chars")
#category form w a3mel validation 3lha 
#validation momkn tb2a fel model bt3 el category mn 3'er form 
    def clean(self):
        super(BookletForm,self).clean()
        content=self.cleaned_data.get('content')
        if len(content) < 10:
            raise ValidationError("minimum length for content is 10 chars")
        return self.cleaned_data



class CategoryForm(forms.ModelForm):
        def clean(self):
            super(CategoryForm,self).clean()
            name=self.cleaned_data.get('name')
            if len(name) < 2:
                raise ValidationError("minimum length for category is 2 chars")
            return self.cleaned_data

