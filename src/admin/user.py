from django.contrib import admin
from src.models.user import UserProfile


@admin.register(UserProfile)
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
