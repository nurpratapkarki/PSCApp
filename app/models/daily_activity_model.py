
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.utils import timezone
import json
class DailyActivity(models.Model):
    """
    Daily platform activity tracking for trend analysis
    Used for charts and growth metrics
    """
    date = models.DateField(
        unique=True,
        help_text="Date of activity tracking"
    )
    new_users = models.IntegerField(
        default=0,
        help_text="New user registrations"
    )
    questions_added = models.IntegerField(
        default=0,
        help_text="New questions added this day"
    )
    questions_approved = models.IntegerField(
        default=0,
        help_text="Questions approved by admins"
    )
    mock_tests_taken = models.IntegerField(
        default=0,
        help_text="Tests started this day"
    )
    total_answers_submitted = models.IntegerField(
        default=0,
        help_text="Question attempts across all users"
    )
    active_users = models.IntegerField(
        default=0,
        help_text="Unique users who performed any action"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'daily_activities'
        verbose_name = 'Daily Activity'
        verbose_name_plural = 'Daily Activities'
        ordering = ['-date']
        indexes = [
            models.Index(fields=['date']),
        ]
    
    def __str__(self):
        return f"Activity: {self.date}"
    
    # TODO: Add method to get activity for date range
    # @staticmethod
    # def get_activity_range(start_date, end_date):
    #     pass
    
    # TODO: Add method to get weekly/monthly trends
    # @staticmethod
    # def get_trend_data(period='week'):
    #     pass
    
    # TODO: Add scheduled task to create/update daily record
    # @staticmethod
    # def record_today_activity():
    #     pass
