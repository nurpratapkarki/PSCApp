from django.contrib import admin
from src.models.app_settings import AppSettings


@admin.register(AppSettings)
class AppSettingsAdmin(admin.ModelAdmin):
    list_display = ("setting_key", "is_active", "updated_at")
    list_filter = ("is_active",)
    search_fields = ("setting_key", "description")
    readonly_fields = ("updated_at",)
