from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.utils.html import format_html

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
    list_per_page = 50

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )


@admin.register(Group, site=CustomAdmin)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(UserProfile, site=CustomAdmin)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        "profile_picture_tag",
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
    readonly_fields = (
        "profile_picture_tag",
        "level",
        "total_contributions",
        "total_questions_attempted",
    )
    date_hierarchy = "date_joined"
    list_per_page = 25
    autocomplete_fields = ["target_branch", "target_sub_branch"]

    def profile_picture_tag(self, obj):
        if obj.profile_picture:
            return format_html(
                '<img src="{}" style="width: 45px; height: 45px; border-radius: 50%; object-fit: cover;" />',
                obj.profile_picture.url,
            )
        return "-"

    profile_picture_tag.short_description = "Avatar"

    fieldsets = (
        (
            "Basic Information",
            {
                "fields": (
                    "google_auth_user",
                    "profile_picture_tag",
                    "full_name",
                    "email",
                    "phone_number",
                    "profile_picture",
                ),
                "description": "Essential user identification and contact details.",
            },
        ),
        (
            "Academic Preferences",
            {
                "fields": ("preferred_language", "target_branch", "target_sub_branch"),
                "description": "User's study goals and language settings.",
            },
        ),
        (
            "Gamification & Progress",
            {
                "fields": (
                    "experience_points",
                    "level",
                    "total_contributions",
                    "total_questions_attempted",
                ),
                "classes": ("collapse",),
                "description": "User's achievement metrics and activity summary.",
            },
        ),
        (
            "Account Status",
            {
                "fields": ("is_active", "date_joined", "last_login"),
                "classes": ("collapse",),
            },
        ),
    )
