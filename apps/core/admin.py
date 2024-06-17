from django.contrib import admin
from django.conf import settings
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

from apps.core.models import Account, SocialNetwork, Profile, AccountLink


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class SocialNetworkInline(admin.StackedInline):
    model = SocialNetwork
    extra = 0


@admin.register(Account)
class AccountAdmin(UserAdmin):
    list_display = ["email", "username", "is_staff", "email_is_confirmed", "created_at"]
    list_filter = ["email", "is_staff"]
    inlines = [ProfileInline, SocialNetworkInline]

    fieldsets = [
        (
            None,
            {"fields": ("email", "username", "password", "first_name", "last_name")},
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "email_is_confirmed",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                ),
            },
        )
    ]

    list_editable = ["email_is_confirmed"]
    search_fields = ["email"]
    ordering = ["email"]


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ["account", "channel", "display_social_newtork_url"]
    list_filter = ["channel"]
    search_fields = [
        "account__username", "account__email", "account__first_name",
        "account__last_name"
    ]
    raw_id_fields = ["account"]
    date_hierarchy = "created_at"
    list_select_related = ["account"]

    @admin.display(description="URL")
    def display_social_newtork_url(self, instance):
        return format_html(
            f"<a target='_blank' href={instance.url}>{instance.url}</a>"
        )


@admin.register(AccountLink)
class AccountLinkAdmin(admin.ModelAdmin):
    list_display = ["account", "title", "display_url"]
    search_fields = [
        "account__username", "account__email", "account__first_name",
        "account__last_name", "title"
    ]
    raw_id_fields = ["account"]
    date_hierarchy = "created_at"
    list_select_related = ["account"]

    @admin.display(description="URL")
    def display_url(self, instance):
        return format_html(
            f"<a target='_blank' href={instance.url}>{instance.url}</a>"
        )


# Custom admin name

title = settings.PROJECT_NAME
full_title = "{} (v{})".format(
    title,
    getattr(settings, "VERSION", "0.1.0"),
)
admin.site.site_title = "Django Admin"
admin.site.site_header = full_title
admin.site.index_title = title
