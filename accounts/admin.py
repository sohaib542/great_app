from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
# Register your models here.
class myadmin(UserAdmin):
    list_display=('email','username','firstname','lastname','last_login','is_active','date_joined')
    list_display_links=('email','username','firstname')
    readonly_fields=('date_joined','last_login')
    ordering=('-date_joined',)
    filter_horizontal=()
    list_filter=()
    fieldsets=()
admin.site.register(Account,myadmin)