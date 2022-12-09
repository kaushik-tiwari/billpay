from django.contrib import admin
from .models import Billform
# Register your models here.


class Filter(admin.ModelAdmin):
    list_display = ('name','bill_data','ExpiryDate','status')
    list_filter = ('status','bill_data')
    search_fields = ('name',)




admin.site.register(Billform,Filter)
