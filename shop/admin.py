from django.contrib import admin
from .models import Category,Product

# Register your models here.
class AdminCategory(admin.ModelAdmin):
    list_display=('nom','date_added')


class AdminProduct(admin.ModelAdmin):
    list_display=('title','price','date_added','category')

admin.site.register(Category,AdminCategory)
admin.site.register(Product,AdminProduct)
 