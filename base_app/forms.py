from django import forms
from .models import ModelFormRegistration


class FormRegistration(forms.ModelForm):
    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={
                               'type': "text", 'name': "name", 'class': "form-control", 'id': "name",
                               'placeholder': "Your Name", 'data-rule': "minlen:4",
                               'data-msg': "Please enter at least 4 chars",
                           }))

    email = forms.EmailField(
        widget=forms.TextInput(attrs={'type': 'email', 'id': 'email', 'name': 'email', 'class': 'form-control',
                                      'placeholder': 'Email', 'required': 'required', 'data-rule': 'email', 'data-msg': 'Please enter a valid email'}))

    phone = forms.CharField(max_length=15,
                                 widget=forms.TextInput(
                                     attrs={'type': 'text', 'name': 'phone', 'id': 'phone', 'class': 'form-control',
                                            'placeholder': 'Телефон', 'required': 'required',
                                            'data-rule': 'minlen:4', 'data-msg': 'Please enter at least 4 chars'}))

    message = forms.CharField(max_length=400,
                                   widget=forms.Textarea(attrs={'type': 'message', 'name': 'message', 'class': 'form-control',
                                                                'rows': '5', 'placeholder': 'Сообщение', 'required': 'required'}))


    class Meta:
        model = ModelFormRegistration
        fields = ('name', 'email', 'phone', 'message')
