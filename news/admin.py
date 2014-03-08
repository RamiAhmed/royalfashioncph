from django.contrib import admin
from news.models import NewsImage, NewsPost
from sorl.thumbnail.admin import AdminImageMixin
from wysihtml5.admin import AdminWysihtml5TextFieldMixin

# Register your models here.
class NewsImageAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ['image_title']    
    search_fields = ['image_title']    
    save_on_top = True
    
class NewsImageInline(admin.StackedInline):
    model = NewsImage
    
class NewsAdmin(AdminWysihtml5TextFieldMixin, admin.ModelAdmin):
    list_display = ['title', 'added', 'active']
    
    list_filter = ['added', 'active']
    
    search_fields = ['title', 'body']
    
    save_on_top = True
    
    prepopulated_fields = {"slug": ('title',)}
    
    inlines = [NewsImageInline,]

    
admin.site.register(NewsImage, NewsImageAdmin)
admin.site.register(NewsPost, NewsAdmin)
    