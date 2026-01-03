from django.contrib import admin
from django.contrib.auth.models import Group, User

from src.admin.custom_admin import CustomAdmin
from src.models.user import UserProfile

# Register default User and Group models with CustomAdmin
admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User, site=CustomAdmin)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    search_fields = ("username", "email", "first_name", "last_name")
    list_filter = ("is_staff", "is_superuser", "is_active")


@admin.register(Group, site=CustomAdmin)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(UserProfile, site=CustomAdmin)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "email",
        "level",
        "experience_points",
        "target_branch",
        "is_active",
    )
    list_filter = ("is_active", "preferred_language", "target_branch", "level")
    search_fields = ("full_name", "email", "phone_number")
    ordering = ("-date_joined",)
    readonly_fields = ("level", "total_contributions", "total_questions_attempted")

    fieldsets = (
        (
            "User Info",
            {
                "fields": (
                    "google_auth_user",
                    "full_name",
                    "email",
                    "phone_number",
                    "profile_picture",
                )
            },
        ),
        (
            "Preferences",
            {"fields": ("preferred_language", "target_branch", "target_sub_branch")},
        ),
        (
            "Gamification",
            {
                "fields": (
                    "experience_points",
                    "level",
                    "total_contributions",
                    "total_questions_attempted",
                )
            },
        ),
        ("Status", {"fields": ("is_active", "date_joined", "last_login")}),
    )
