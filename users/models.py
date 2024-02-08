from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

def user_directory_path(instance, filename):
    return 'users/{0}'.format(filename)
class User(AbstractUser):
    image=models.ImageField(upload_to=user_directory_path,blank=True,null=True,verbose_name="Аватар")

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