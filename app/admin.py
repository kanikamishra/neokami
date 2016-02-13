from django.contrib import admin

# Register your models here.
from app.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('contact','first_name','last_name','email')

admin.site.register(Contact,ContactAdmin)