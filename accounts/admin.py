from django.contrib import admin
from .models import *


class UserAccounts(admin.ModelAdmin):
    list_display=('email', 'first_name', 'last_name')
admin.site.register(UserAccount, UserAccounts)