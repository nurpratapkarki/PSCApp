from django.contrib import admin
from src.models.branch import Branch, SubBranch, Category


class SubBranchInline(admin.TabularInline):
    model = SubBranch
    extra = 1
    prepopulated_fields = {"slug": ("name_en",)}


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = (
        "name_en",
        "name_np",
        "has_sub_branches",
        "is_active",
        "display_order",
    )
    list_editable = ("is_active", "display_order")
    search_fields = ("name_en", "name_np")
    prepopulated_fields = {"slug": ("name_en",)}
    inlines = [SubBranchInline]


@admin.register(SubBranch)
class SubBranchAdmin(admin.ModelAdmin):
    list_display = ("name_en", "branch", "is_active", "display_order")
    list_filter = ("branch", "is_active")
    search_fields = ("name_en", "name_np")
    prepopulated_fields = {"slug": ("name_en",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name_en",
        "scope_type",
        "target_branch",
        "category_type",
        "is_public",
        "is_active",
    )
    list_filter = (
        "scope_type",
        "category_type",
        "is_public",
        "is_active",
        "target_branch",
    )
    search_fields = ("name_en", "name_np", "description_en")
    prepopulated_fields = {"slug": ("name_en",)}
    autocomplete_fields = ["target_branch", "target_sub_branch", "created_by"]
