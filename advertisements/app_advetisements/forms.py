from .models import Advertisements
from django.forms import ModelForm, Textarea, TextInput, NumberInput, CheckboxInput, FileInput
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AdvertisementForm(ModelForm):
    class Meta:
        model = Advertisements
        fields = ['title', 'description', 'price', 'auction', 'image',]
        widgets = {
                'title' : TextInput(attrs = {'class' : 'form-control form-control-lg'}),
                'description' : Textarea(attrs = {'class' : 'form-control form-control-lg'}),
                'price' : NumberInput(attrs = {'class' : 'form-control form-control-lg'}),
                'auction' : CheckboxInput(attrs = {'class' : 'form-control form-check-input'}),
                'image' : FileInput(attrs = {'class' : 'form-control form-control-lg'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if title.startswith('?'):
            raise ValidationError('Заголовок начинаеся в вопросительного знака!')
        return title