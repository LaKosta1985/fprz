from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
CHOICES = (
        ('admin', 'admin'),
        ('prezident', 'prezident'),
        ('secret', 'secret'),
        ('antidoping', 'antidoping'),
         ('free', 'free'),
    )
CHOICES_Fed = (
        ('true', 'член федерации'),
        ('false', 'не состоит'),
    )
def user_directory_path(instance, filename):
    return 'users/{0}'.format(filename)
class User(AbstractUser):
    image=models.ImageField(upload_to=user_directory_path,blank=True,null=True,verbose_name="Аватар")
    tel=models.CharField(max_length=20,verbose_name="Телефон",blank=True,null=True)
    status=models.CharField(choices=CHOICES,verbose_name="Статус",blank=True,null=True,default='free')
    status_in_Feder=models.CharField(choices=CHOICES_Fed,verbose_name="Член Федерации?",blank=True,null=True)
class Meta: 
        db_table = 'пользователь'
        verbose_name = 'Пользователь'  
        verbose_name_plural = 'Пользователи'
     

def __str__(self):
        return self.title

@receiver(pre_delete, sender=User)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)



    