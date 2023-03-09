from django.contrib import admin
from .models import  Category,Post
# Register your models here.



# For Configuration Of Your Category Admin

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('Image_tag','Title', 'Description', 'Url', 'Add_date')
    search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('Title','url','Cat')
    search_fields = ('Title',)
    list_filter = ('Cat',)
    list_per_page = 1

#class Media:
 #   JS= ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js', 'js/script.js',)


admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)