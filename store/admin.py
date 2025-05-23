from django.contrib import admin
from .models import Product
# Register your models here.


class productadmin(admin.ModelAdmin):
    list_display=('product_name','price','stock','category','modified_date','is_avaliable')
    prepopulated_fields={'slug':('product_name',)}

admin.site.register(Product,productadmin)