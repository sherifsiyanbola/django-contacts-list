from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'email', 'info', 'phone')
    list_per_page = 5
    list_display_links = ('email','name')
    list_editable = ('info','gender')
    search_fields = ('name', 'gender', 'email', 'info', 'phone')
    list_filter = ('gender', 'info', 'date_added')
    
admin.site.register(Contact, ContactAdmin)
# admin.site.unregister(Group)
