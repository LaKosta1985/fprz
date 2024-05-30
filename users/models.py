from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.urls import reverse
from fprz.settings import CHOICES_category,CHOICES,CHOICES_Fed,CHOICES_RAZRAD

def user_directory_path(instance, filename):
    return 'users/{0}'.format(filename)
class User(AbstractUser):
    slug=models.SlugField(max_length=255,verbose_name="URL-не обязательно к заполнению, дублируется на латинице",unique=True,db_index=True,default='free')
    image=models.ImageField(upload_to=user_directory_path,blank=True,null=True,verbose_name="Аватар")
    tel=models.CharField(max_length=20,verbose_name="Телефон",blank=True,null=True)
    status=models.CharField(choices=CHOICES,verbose_name="Статус",blank=True,null=True,default='free')
    status_in_Feder=models.CharField(choices=CHOICES_Fed,verbose_name="Член Федерации?",blank=True,null=True)
    bench=models.CharField(verbose_name="Ваш максимальный соревновательный присед",blank=True,null=True)
    press=models.CharField(verbose_name="Ваш максимальный соревновательный жим",blank=True,null=True)
    d_lift=models.CharField(verbose_name="Ваш максимальная соревновательная тяга",blank=True,null=True)
    sum=models.CharField(verbose_name="Ваша максимальная сумма",blank=True,null=True)
    kat=models.CharField(choices=CHOICES_category ,verbose_name="Ваша категория")
    raz=models.CharField(choices=CHOICES_RAZRAD ,verbose_name="Ваша разряд",blank=True,null=True)
    therd_name=models.CharField(verbose_name="Вашe отчество",blank=True,null=True)
    date = models.DateField(blank=True, null=True, verbose_name="Дата рождения")  
    from_self = models.TextField(verbose_name="О себе",blank=True, null=True)  
class Meta: 
        db_table = 'пользователь'
        verbose_name = 'Пользователь'  
        verbose_name_plural = 'Пользователи'
def get_absolute_url(self):
        return reverse("mailPost", kwargs={"slug_status": self.slug})    

def __str__(self):
        return self.title

@receiver(pre_delete, sender=User)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)



    