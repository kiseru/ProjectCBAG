from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', max_length=20,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
