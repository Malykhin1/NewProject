from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import News, Category


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = News
        fields = '__all__'

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'content', 'created_at', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'content')
    list_filter = ('is_published', 'id')
    list_editable = ('is_published', 'category')
    fields = ('title', 'content', 'photo', 'get_photo', 'is_published', 'created_at', 'updated_at',)
    readonly_fields = ('get_photo', 'created_at', 'updated_at')
    form = NewsAdminForm

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return 'Фото нет'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title') #Поля которые будут отображаться в админке
    list_display_links = ('id','title') #В каких полях будут ссылки записи


#Регистрация моделей в админке
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)



