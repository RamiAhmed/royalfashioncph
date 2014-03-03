from django.contrib import admin

from shop.models import ProductImage, ProductSize, Product, Collection

from sorl.thumbnail.admin import AdminImageMixin

# Register your models here.
class ProductImageAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ['image_title']    
    search_fields = ['image_title']    
    save_on_top = True
    
class ProductImageInline(admin.StackedInline):
    model = ProductImage
    
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ['size']
    search_fields = ['size']
    save_on_top = True
    
class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'added', 'for_sale']
    
    list_filter = ['added', 'for_sale']
    
    search_fields = ['name', 'price', 'description']
    
    save_on_top = True
    
    prepopulated_fields = {"slug": ('name',)}
    
    inlines = [ProductImageInline,ProductSizeInline,]

#class ProductInline(admin.StackedInline):
#    model = Product
#    extra = 3

class CollectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'added', 'active']
    
    list_filter = ['added', 'active']
    
    search_fields = ['name']
    
    date_hierarchy = 'added'
    
    save_on_top = True
    
    prepopulated_fields = {"slug": ('name',)}

    #inlines = [ProductInline,]

admin.site.register(ProductSize, ProductSizeAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Collection, CollectionAdmin)
