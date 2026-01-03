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
    )
    list_filter = ("test_type", "is_active", "is_public", "branch")
    search_fields = ("title_en", "title_np")
    prepopulated_fields = {"slug": ("title_en",)}
    inlines = [MockTestQuestionInline]
