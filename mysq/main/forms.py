from django import forms
from django.forms import TextInput, NumberInput, Select, ChoiceField
from django.contrib.auth.models import User
from .models import Dots


class LoginForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Пользователь с логином {username} не найден в системе.')
        user = User.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError("Неверный пароль")
            return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password']

        widgets = {
            "username": TextInput(attrs={
                'class': 'login-form',
                'placeholder': 'Введите логин...'
            }),
            "password": TextInput(attrs={
                'class': 'login-form',
                'placeholder': 'Введите пароль...'
            })
        }


class RegistrationForm(forms.ModelForm):

    confirm_password = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'
        self.fields['confirm_password'].label = 'Подтвердите пароль'
        self.fields['first_name'].label = 'Ваше имя'
        self.fields['last_name'].label = 'Ваша фамилия'

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Имя {username} занято')
        return username

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Пароли не совпадают')
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password', 'first_name', 'last_name']


class DotsForm(forms.ModelForm):
    CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )

    r_value = ChoiceField(choices=CHOICES)

    class Meta:
        model = Dots
        fields = ['x_value', 'y_value', 'r_value', 'result']

        widgets = {
            'x_value': NumberInput(attrs={
                'class': 'form-control',
                'id': 'X',
                'placeholder': 'Введите значение X'
            }),
            'y_value': NumberInput(attrs={
                'class': 'form-control',
                'id': 'Y',
                'placeholder': 'Введите значение Y'
            })
        }

