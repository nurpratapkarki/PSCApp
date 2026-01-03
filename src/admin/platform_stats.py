from django.contrib import admin

from src.admin.custom_admin import CustomAdmin
from src.models.platform_stats import PlatformStats
from src.models.time_configuration import TimeConfiguration


@admin.register(TimeConfiguration, site=CustomAdmin)
class TimeConfigurationAdmin(admin.ModelAdmin):
    list_display = (
        "branch",
        "sub_branch",
        "category",
        "standard_duration_minutes",
        "questions_count",
        "is_active",
    )
    list_filter = ("branch", "is_active")
    search_fields = ("description", "branch__name_en")
    autocomplete_fields = ["branch", "sub_branch", "category"]

    fieldsets = (
        (
            "Targeting",
            {
                "fields": ("branch", "sub_branch", "category"),
            },
        ),
        (
            "Configuration",
            {
                "fields": (
                    "standard_duration_minutes",
                    "questions_count",
                    "marks_per_question",
                    "negative_marks_per_question",
                ),
            },
        ),
        (
            "Status",
            {
                "fields": ("is_active", "description"),
            },
        ),
    )


@admin.register(PlatformStats, site=CustomAdmin)
class PlatformStatsAdmin(admin.ModelAdmin):
    list_display = (
        "last_updated",
        "total_users_active",
        "total_questions_public",
        "total_mock_tests_taken",
        "total_answers_submitted",
    )
    readonly_fields = (
        "total_questions_public",
        "total_questions_pending",
        "total_contributions_this_month",
        "total_users_active",
        "total_mock_tests_taken",
        "total_answers_submitted",
        "questions_added_today",
        "top_contributor_this_month",
        "most_attempted_category",
        "last_updated",
    )

    fieldsets = (
        (
            "Content Metrics",
            {
                "fields": (
                    "total_questions_public",
                    "total_questions_pending",
                    "questions_added_today",
                    "most_attempted_category",
                ),
            },
        ),
        (
            "User & Community",
            {
                "fields": (
                    "total_users_active",
                    "total_contributions_this_month",
                    "top_contributor_this_month",
                ),
            },
        ),
        (
            "Usage Statistics",
            {
                "fields": ("total_mock_tests_taken", "total_answers_submitted"),
            },
        ),
        (
            "Metadata",
            {
                "fields": ("last_updated",),
            },
        ),
    )

    def has_add_permission(self, request):
        return False
