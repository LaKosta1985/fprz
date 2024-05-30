from django import forms
from .models import *
from captcha.fields import CaptchaField
from fprz.settings import CHOICES_EKIP,CHOICES_RAZRAD,CHOICES_category
class ZayavkaForm(forms.Form):
    namesor = forms.CharField(widget=forms.Textarea(attrs={'rows':2}),label="Название соревнований:")
    name = forms.CharField(min_length=2,max_length=30,label="Имя:")
    lastname=forms.CharField(min_length=2,max_length=30,label="Фамилия:")
    thirdname=forms.CharField(min_length=2,max_length=30,label="Отчество:")
    date=forms.DateField(label="Дата рождения:",widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'dd-mm-yyyy', 'class': 'custom-class'}))
    dv=forms.ChoiceField(choices=CHOICES_EKIP,label="Дивизион:")
    raz=forms.ChoiceField(choices=CHOICES_RAZRAD,label="Разряд/Звание:")
    kat=forms.ChoiceField(choices=CHOICES_category,label="Категория:")
    tren=forms.CharField(min_length=2,max_length=30,label="Имя тренера\лично")
    email=forms.EmailField(label="Ваша почта")
    tel=forms.CharField(min_length=2,max_length=30,label="Ваш телефон")
    rez=forms.CharField(widget=forms.Textarea(attrs={'rows':2}),label="Лучший результат, где показан (в течение года)")
    captcha=CaptchaField(label="Введите отображенные буквы, с учетом регистра")


class MesForm(forms.Form):
    name = forms.CharField(min_length=2,max_length=30,label="Ваше Имя:")
    email=forms.EmailField(label="Ваша почта")
    text_mes = forms.CharField(widget=forms.Textarea(attrs={'rows':2}),label="Текст письма:")
    captcha=CaptchaField(label="Введите отображенные буквы, с учетом регистра")

