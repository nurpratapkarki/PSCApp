from django.contrib import admin
from src.models.user_stats import UserStatistics, UserProgress, StudyCollection


@admin.register(UserStatistics)
class UserStatisticsAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "study_streak_days",
        "questions_answered",
        "correct_answers",
        "accuracy_rank",
    )
    search_fields = ("user__email",)
    readonly_fields = ("badges_earned",)


@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "category",
        "accuracy_percentage",
        "questions_attempted",
    )
    list_filter = ("category",)
    search_fields = ("user__email",)


@admin.register(StudyCollection)
class StudyCollectionAdmin(admin.ModelAdmin):
    list_display = ("name", "created_by", "is_private", "get_question_count")
    list_filter = ("is_private",)
    filter_horizontal = ("questions",)
