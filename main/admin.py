from django import forms
from django.contrib import admin
from main.models import New,Doc,Table_Norm,Table_Cat,Calendar,Table_Cat_Record,Table_Record,Foto
from django.utils.safestring import mark_safe
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class NewAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(),label="Ввод текста новости")
    class Meta:
        model = New
        fields = '__all__'





@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):
    list_display=("id","title","name","get_image")# метод для отображения категорий
    list_filter=("title","name")# метод для фильтраций по разделам
    list_display_links=('title',) # метод для ссылок на конкретную запись
    search_fields=('title',) # метод для поиска категорий
    def get_image(self,obj):
        return mark_safe(f'<img src={obj.image.url}  height="50"')
    get_image.short_description="Обложка"
   
  
    

@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    form=NewAdminForm

admin.site.register(Doc)
admin.site.register(Table_Norm)
admin.site.register(Table_Cat)
admin.site.register(Calendar)
admin.site.register(Table_Record)
admin.site.register(Table_Cat_Record)






