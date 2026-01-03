from django.contrib import admin

from src.admin.custom_admin import CustomAdmin
from src.models.analytics import Contribution, DailyActivity, LeaderBoard


@admin.register(Contribution, site=CustomAdmin)
class ContributionAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "question",
        "contribution_year",
        "contribution_month",
        "status",
        "is_featured",
    )
    list_filter = ("status", "is_featured", "contribution_year", "contribution_month")
    search_fields = ("user__email", "user__username")
    actions = ["approve_contribution", "make_public", "reject_contribution"]

    fieldsets = (
        (
            "Core Details",
            {
                "fields": ("user", "question", "status"),
            },
        ),
        (
            "Period & Features",
            {
                "fields": ("contribution_year", "contribution_month", "is_featured"),
            },
        ),
        (
            "Metadata",
            {
                "fields": ("created_at", "updated_at"),
                "classes": ("collapse",),
            },
        ),
    )

    @admin.action(description="Approve selected contributions")
    def approve_contribution(self, request, queryset):
        for contribution in queryset:
            contribution.approve_contribution()
        self.message_user(request, f"{queryset.count()} contributions approved.")

    @admin.action(description="Make selected contributions Public")
    def make_public(self, request, queryset):
        for contribution in queryset:
            contribution.make_public()
        self.message_user(request, f"{queryset.count()} contributions made public.")


@admin.register(LeaderBoard, site=CustomAdmin)
class LeaderBoardAdmin(admin.ModelAdmin):
    list_display = (
        "rank",
        "user",
        "total_score",
        "branch",
        "time_period",
    )
    list_filter = ("time_period", "branch")
    search_fields = ("user__email",)
    ordering = ("time_period", "branch", "rank")


@admin.register(DailyActivity, site=CustomAdmin)
class DailyActivityAdmin(admin.ModelAdmin):
    list_display = (
        "date",
        "new_users",
        "questions_added",
        "mock_tests_taken",
        "active_users",
    )
    ordering = ("-date",)
