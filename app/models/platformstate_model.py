from django.db import models
from .user_model import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.utils import timezone
import json

class PlatformStats(models.Model):
    """
    Global platform statistics for public dashboard
    Shows community activity and engagement
    Singleton model - only one active record
    """
    total_questions_public = models.IntegerField(
        default=0,
        help_text="All approved public questions"
    )
    total_questions_pending = models.IntegerField(
        default=0,
        help_text="Waiting for monthly approval"
    )
    total_contributions_this_month = models.IntegerField(
        default=0,
        help_text="Contributions in current month (resets monthly)"
    )
    total_users_active = models.IntegerField(
        default=0,
        help_text="Users who contributed/attempted in last 30 days"
    )
    total_mock_tests_taken = models.IntegerField(
        default=0,
        help_text="All time test attempts"
    )
    total_answers_submitted = models.IntegerField(
        default=0,
        help_text="Total question attempts across platform"
    )
    questions_added_today = models.IntegerField(
        default=0,
        help_text="Questions added in last 24 hours"
    )
    top_contributor_this_month = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='top_contributor_stats'
    )
    most_attempted_category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='top_category_stats'
    )
    last_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'platform_stats'
        verbose_name = 'Platform Statistics'
        verbose_name_plural = 'Platform Statistics'
    
    def __str__(self):
        return f"Platform Stats (Updated: {self.last_updated})"
    
    # TODO: Add method to refresh all statistics
    # def refresh_stats(self):
    #     pass
    
    # TODO: Add method to reset monthly counters
    # def reset_monthly_stats(self):
    #     pass
    
    # TODO: Add scheduled task to update stats every hour
    # @staticmethod
    # def scheduled_update():
    #     pass
