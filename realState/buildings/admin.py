from django.contrib import admin
from .models import *
# Register your models here.
class HomeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}  # new
    list_display = ("title","city","state","is_published",)
    list_editable = ("is_published",)
    
admin.site.register(Home,HomeAdmin)
admin.site.register(ImageFiles)