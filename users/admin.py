from django.contrib import admin
from users.models import User
from django.utils.safestring import mark_safe


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=("id","slug","first_name","last_name","get_image","tel","status","status_in_Feder","date")# метод для отображения категорий
    list_display_links=('id',"slug",'first_name','last_name')
    prepopulated_fields={'slug':('status',)}
    def get_image(self,obj):
        if obj.image:
            return mark_safe(f'<img src={obj.image.url}  height="50"')
        else:
            return mark_safe(f'<img src="/static/load/users/no-photo.jpg"  height="50"')
    get_image.short_description="Аватар"




  

