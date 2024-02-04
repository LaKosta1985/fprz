from django.db import models
from django_resized import ResizedImageField

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'news/{0}/{1}'.format(instance.title,filename)

class New(models.Model):
    title = models.CharField(max_length=100,verbose_name="Заголовок")
    content = models.TextField(max_length=2000,verbose_name="Текст")
    img_Head = ResizedImageField(upload_to=user_directory_path)
    date=models.DateTimeField(blank=True,null=True)
    count_view=models.IntegerField(blank=True,null=True)
    img_Body=models.ImageField(upload_to=user_directory_path,blank=True,null=True)
    video=models.URLField(blank=True,null=True)

    class Meta: 
        db_table = 'new'
        verbose_name = 'Новость'  
        verbose_name_plural = 'Новости'
     

    def __str__(self):
        return self.title




