from django.contrib import admin
from .models import Links,User,AdminInfo
# Register your models here.


@admin.register(AdminInfo)
class AdminInfo(admin.ModelAdmin):
    list_display=['id','email','password','date_created']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','email','password','date_created']

@admin.register(Links)
class LinkAdmin(admin.ModelAdmin):
    list_display=['id','link','email','date_created','password']

