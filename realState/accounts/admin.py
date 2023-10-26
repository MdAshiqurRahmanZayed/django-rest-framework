from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# admin.py
from django.contrib import admin
from django.contrib.admin import AdminSite



class CustomUserAdmin(UserAdmin):
    model = User
    list_display =('email','username','last_login','is_active')
     
    list_display_links =('email',)
     # readonly_fields = ('last_login','date_joined')
    ordering = ('-id',)
    filter_horizontal =()
    list_filter = ()  
    # Customize the label for the email field
    fieldsets = (
        (None, {'fields': ('username', 'password',)}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',)}),
        ('Important dates', {'fields': ('last_login',)}),
    )

admin.site.register(User,CustomUserAdmin) 

