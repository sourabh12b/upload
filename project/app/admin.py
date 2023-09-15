from django.contrib import admin
from .models import *
from django.contrib.sessions.models import Session

class show(admin.ModelAdmin):
    list_display=('id','name','image','price','quantity','available','desc')

class show1(admin.ModelAdmin):
    list_display=('id','name','email','message')

class show2(admin.ModelAdmin):
    list_display=('id','user','cat','cat_id','purchased_quan','date')


admin.site.register(earbud,show)
admin.site.register(contact,show1)
admin.site.register(transaction,show2)
admin.site.register(ItemModel)

# Register your models here.
