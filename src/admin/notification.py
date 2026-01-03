from django.contrib import admin

from src.admin.custom_admin import CustomAdmin
from src.models.notification import Notification


@admin.register(Notification, site=CustomAdmin)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "notification_type",
        "title_en",
        "is_read",
        "created_at",
    )
    list_filter = ("notification_type", "is_read", "created_at")
    list_editable = ("is_read",)
    search_fields = ("user__email", "title_en", "message_en")
    readonly_fields = ("created_at",)
    date_hierarchy = "created_at"
    list_per_page = 50
    autocomplete_fields = ["user"]
