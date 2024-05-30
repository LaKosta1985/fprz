from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm 
from users.models import User
from captcha.fields import CaptchaField
from fprz.settings import CHOICES_category,CHOICES_RAZRAD
class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()
    class Meta():
        model=User

class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "therd_name",
            "username",
            "email",
            "tel",
            "status",
            "password1",
            "password2",
        )
    
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    therd_name=forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    tel = forms.CharField(required=False)
    status = forms.CharField(required=False)
    password1 = forms.CharField()
    password2 = forms.CharField()

class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "image",
            "first_name",
            "last_name",
            "therd_name",
            "date",
            "username",
            "email",
            "tel",
            "bench",
            "press",
            "d_lift",
            "sum",
            "kat",
            "raz",
            "from_self",
            "status",)

    image = forms.ImageField(required=False)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    therd_name = forms.CharField(required=False)
    username = forms.CharField()
    email = forms.CharField(required=False)
    tel = forms.CharField(required=False)
    bench=forms.CharField(required=False)
    press=forms.CharField(required=False)
    d_lift=forms.CharField(required=False)
    sum=forms.CharField(required=False)
    kat=forms.ChoiceField(required=False,choices=CHOICES_category,label="Категория:")
    raz=forms.ChoiceField(required=False,choices=CHOICES_RAZRAD,label="Разряд/Звание:")
    date=forms.DateField(required=False,label="Дата рождения:",widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'dd-mm-yyyy', 'class': 'custom-class'}))
    from_self=forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    status = forms.CharField(required=False)


class SendPassToEmail(forms.Form):
    email=forms.EmailField(label="Напишите почту указанную при регистрации, на нее придет пароль")
    captcha=CaptchaField(label="Введите отображенные буквы, с учетом регистра")