from django.contrib import admin
from .models import Member
# Register your models here.

class AdminMember(admin.ModelAdmin):
    list_display=("firstname","lastname","dob")

# admin.site.register(Member)
admin.site.register(Member,AdminMember)