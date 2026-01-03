from django.contrib import admin

from src.admin.custom_admin import CustomAdmin
from src.models.mocktest import MockTest, MockTestQuestion


class MockTestQuestionInline(admin.TabularInline):
    model = MockTestQuestion
    raw_id_fields = ("question",)
    extra = 1


@admin.register(MockTest, site=CustomAdmin)
class MockTestAdmin(admin.ModelAdmin):
    list_display = (
        "title_en",
        "test_type",
        "branch",
        "total_questions",
        "is_active",
        "is_public",
        "created_at",
    )
    list_filter = ("test_type", "is_active", "is_public", "branch")
    list_editable = ("is_active", "is_public")
    search_fields = ("title_en", "title_np")
    prepopulated_fields = {"slug": ("title_en",)}
    inlines = [MockTestQuestionInline]
    date_hierarchy = "created_at"
    list_per_page = 30

    fieldsets = (
        (
            "General Information",
            {
                "fields": ("title_en", "title_np", "slug", "test_type"),
            },
        ),
        (
            "Configuration",
            {
                "fields": (
                    "branch",
                    "time_limit_minutes",
                    "total_marks",
                    "pass_percentage",
                ),
            },
        ),
        (
            "Status & Visibility",
            {
                "fields": ("is_active", "is_public"),
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
