from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Адрес электронной почты", widget=forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'motte_vessale@mail.ru'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['username'].widget.attrs['placeholder'] = 'Matvei'
        self.fields['username'].label = 'Имя пользователя'
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>*Не более 150 символов. Только буквы, цифры и @/./+/-/_.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['password1'].widget.attrs['placeholder'] = 'Veselove123'
        self.fields['password1'].label = 'Пароль'
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Ваш пароль не должен быть слишком похож на другую вашу личную информацию.</li><li>Ваш пароль должен содержать не менее 8 символов.</li><li>Ваш пароль не может быть часто используемым паролем.</li><li>Ваш пароль не может быть полностью цифровым.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['password2'].widget.attrs['placeholder'] = 'Veselove123'
        self.fields['password2'].label = 'Подтверждение пароля'
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>*Введите тот же пароль, что и раньше, для проверки.</small></span>'