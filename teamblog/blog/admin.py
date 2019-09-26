from django.contrib import admin
from .models import *
# Register your models here.
class user(admin.ModelAdmin):
    list_display = ('username','loginname','url','isActive')
    list_filter = ('username','loginname','url')
    fieldsets = (  ('分组名',{'fields':('username','loginname'),'classes':('collapse',)}),)
class message(admin.ModelAdmin):
    list_display = ('author','time','about','reason','imgs')
    list_filter = ('author','time')
    fieldsets = (('分组名', {'fields': ('author','time'), 'classes': ('collapse',)}),)
class topic(admin.ModelAdmin):
    list_display = ('title','content','select')
    list_filter = ('title','content')
    fieldsets = (('分组名', {'fields': ('title', 'content'), 'classes': ('collapse',)}),)
admin.site.register(User,user)
admin.site.register(Message,message)
admin.site.register(Topic,topic)