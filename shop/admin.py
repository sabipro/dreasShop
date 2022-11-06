from django.contrib import admin
from .models import Category,Product,Commande

# Register your models here.
admin.site.site_header="Kim shop"
admin.site.site_title = "Kim shop"
admin.site.index_title = "Manageur"
class AdminCategory(admin.ModelAdmin):
    list_display=('nom','date_added')




class AdminProduct(admin.ModelAdmin):
    list_display=('title','price','date_added','category')
    search_fields=('title',)
    list_editable = ('price',)

class AdminCommande(admin.ModelAdmin):
    list_display=('items','nom','email','address','ville','pays', 'total','date_commande')

admin.site.register(Category,AdminCategory)
admin.site.register(Product,AdminProduct)
admin.site.register(Commande,AdminCommande)
 