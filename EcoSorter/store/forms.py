from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Matvei'
        self.fields['username'].label = 'Имя пользователя'
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Обязательно*</small></span>'

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'motte_vessale@mail.ru'
        self.fields['email'].label = 'Адрес электронной почты'
        self.fields['email'].help_text = '<span class="form-text text-muted"><small>Обязательно*</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Veselove123'
        self.fields['password1'].label = 'Пароль'
        self.fields['password1'].help_text = '<span class="form-text text-muted"><small>Обязательно*</small></span>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Veselove123'
        self.fields['password2'].label = 'Подтверждение пароля'
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Обязательно*</small></span>'