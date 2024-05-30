from django import forms
from django.contrib import admin
from main.models import *
from django.utils.safestring import mark_safe
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class NewAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(),label="Ввод текста новости")
    class Meta:
        model = New
        fields = '__all__'
class AntiAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(),label="Ввод текста новости")
    class Meta:
        model = Anti
        fields = '__all__'
@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    form=NewAdminForm
    list_display=("id","title","is_published","get_image")# метод для отображения категорий
    list_filter=("title","content")# метод для фильтраций по разделам
    list_display_links=('title',"id") # метод для ссылок на конкретную запись
    search_fields=('title',"content") # метод для поиска категорий
    def get_image(self,obj):
        return mark_safe(f'<img src={obj.img_Head.url}  height="50"')
    get_image.short_description="Обложка"

@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):
    list_display=("id","slug","title","name","get_image")# метод для отображения категорий
    list_filter=("title","name")# метод для фильтраций по разделам
    list_display_links=('title',) # метод для ссылок на конкретную запись
    search_fields=('title',) # метод для поиска категорий
    prepopulated_fields={'slug':('title',)}
    def get_image(self,obj):
        return mark_safe(f'<img src={obj.image.url}  height="50"')
    get_image.short_description="Обложка"
   
@admin.register(Polog)
class PologAdmin(admin.ModelAdmin):
    list_display=("title","is_published")# метод для отображения категорий
    list_filter=("title",)# метод для фильтраций по разделам
    list_display_links=('title',) # метод для ссылок на конкретную запись
    search_fields=('title',) # метод для поиска категорий
  

    



admin.site.register(Table_Norm)
admin.site.register(Table_Cat)
admin.site.register(Calendar)
admin.site.register(Table_Record)

@admin.register(Table_Cat_Record)
class Table_Cat_RecordAdmin(admin.ModelAdmin):
     verbose_name = "Таблица Рекорда"
     verbose_name_plural="Таблицы Рекордов"


admin.site.register(Protocol)

@admin.register(Anti)
class AntiAdmin(admin.ModelAdmin):
    form=AntiAdminForm
    list_display=("id","title","is_published","get_image")# метод для отображения категорий
    list_filter=("title","content")# метод для фильтраций по разделам
    list_display_links=('title',"id") # метод для ссылок на конкретную запись
    search_fields=('title',"content") # метод для поиска категорий
    def get_image(self,obj):
        return mark_safe(f'<img src={obj.img_Head.url}  height="50"')
    get_image.short_description="Обложка"
    


@admin.register(Doc)
class DocAdmin(admin.ModelAdmin):
    list_display=('id','title','time_create','time_update','is_published')
    list_display_links=('id',)
    search_fields=('title',)
    list_editable=('is_published','title')
    list_filter=('is_published','time_create','title')
    
admin.site.site_header='Админ панель сайта FPRZ'
