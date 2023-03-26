from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    email = forms.CharField(required=True, label='Логин')
    password = forms.CharField(required=True, label='Пароль', widget=forms.PasswordInput)


GENDER = \
    (('male', 'Мужской'),
     ('female', 'Женский'))

class CustomUserCreationForm(forms.ModelForm):
    username = forms.CharField(label='Логин')
    email = forms.EmailField(label='почта')
    avatar = forms.ImageField(required=True)
    phone = forms.CharField(label='Номер телефона')
    gender = forms.ChoiceField(label='Пол', choices=GENDER)
    password = forms.CharField(label='Пароль', strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Подтвердите пароль', strip=False, required=True,
                                       widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = (
        'username', 'password', 'password_confirm', 'first_name', 'last_name', 'email', 'avatar', 'birth_date', 'gender')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают!')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        user.groups.add('user')
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'avatar', 'birth_date', 'gender','phone')
        labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'email': 'Email', 'gender': ' Пол','phone':'Номер телефона'}
