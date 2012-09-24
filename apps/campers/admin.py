from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from apps.campers.models import Camper, AccountRequest

class BaseAdmin(admin.ModelAdmin):
        actions_on_top = True

class CamperInline(admin.StackedInline):
    model = Camper
    can_delete = False


class UserAdmin(UserAdmin):
    inlines = (CamperInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class AccountRequestAdmin(BaseAdmin):
    list_display = ('username', 'email', 'timestamp')
    list_display_links = ('username', 'email')


admin.site.register(AccountRequest, AccountRequestAdmin)
