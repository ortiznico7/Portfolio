from django.contrib import admin
from .models import Member, Account

class AccountAdmin(admin.ModelAdmin):
    list_display = ('member', 'account')
    list_filter = ('account')
    search_fields = ('member')

admin.site.register(Member)
admin.site.register(Account)
# Register your models here.
