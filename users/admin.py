from django.contrib import admin
from users.models import User
from django.utils.safestring import mark_safe


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=("id","first_name","last_name","get_image","tel","status","status_in_Feder","date")# метод для отображения категорий
    list_display_links=('id','first_name','last_name')
    def get_image(self,obj):
        if obj.image:
            return mark_safe(f'<img src={obj.image.url}  height="50"')
        else:
            return mark_safe(f'<img src="/static/load/users/no-photo.jpg"  height="50"')
    get_image.short_description="Аватар"




  

