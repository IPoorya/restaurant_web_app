from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import Group
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ["email", "name", "phone_number",
                    "date_joined", "last_login", "is_admin"]
    list_filter = ["date_joined", "last_login", "is_admin"]
    readonly_fields = ["date_joined", "last_login"]
    fieldsets = [
        (None,
         {
             "fields": ["email", "name", "phone_number", "password"]}),
        ("Permissions",
         {
             "fields": ["is_admin", "is_active", "date_joined", "last_login"]}),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "phone_number", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email", "name", "phone_number"]
    ordering = []
    filter_horizontal = []


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
