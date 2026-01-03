from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.utils import timezone
import json

class AppSettings(models.Model):
    """
    Flexible key-value store for system-wide configurations
    Allows changing settings without code deployment
    """
    setting_key = models.CharField(
        max_length=255,
        unique=True,
        help_text="e.g., 'monthly_publication_day', 'min_questions_for_featured'"
    )
    setting_value = models.TextField(
        help_text="JSON string or simple value"
    )
    description = models.TextField(
        null=True,
        blank=True,
        help_text="What this setting controls"
    )
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'app_settings'
        verbose_name = 'App Setting'
        verbose_name_plural = 'App Settings'
        ordering = ['setting_key']
    
    def __str__(self):
        return f"{self.setting_key}: {self.setting_value[:50]}"
    
    # TODO: Add method to get setting value with default
    # @staticmethod
    # def get_setting(key, default=None):
    #     pass
    
    # TODO: Add method to set setting value
    # @staticmethod
    # def set_setting(key, value, description=None):
    #     pass
    
    # TODO: Add method to get JSON setting as dict
    # @staticmethod
    # def get_json_setting(key):
    #     pass


# ============================================================================
# SIGNALS & ADDITIONAL NOTES
# ============================================================================

"""
IMPORTANT: You'll need to create Django signals (signals.py) for:

1. Post-save on UserAnswer:
   - Update Question.times_attempted and times_correct
   - Update UserProgress for the category
   - Update UserStatistics
   - Check and award badges

2. Post-save on Contribution:
   - Update UserProfile.total_contributions
   - Create notification when approved
   - Schedule question for monthly publication

3. Post-save on UserAttempt (when completed):
   - Update LeaderBoard entries
   - Update UserStatistics.mock_tests_completed
   - Create milestone notifications if thresholds reached

4. Daily cron job:
   - Update PlatformStats
   - Create DailyActivity record
   - Check and update user streaks
   - Process scheduled question publications

5. Monthly cron job:
   - Publish approved contributions
   - Reset monthly counters in PlatformStats
   - Generate Facebook shoutout list
   - Archive old leaderboard data

TODO: Create management commands for:
- python manage.py update_platform_stats
- python manage.py process_monthly_publications
- python manage.py recalculate_leaderboards
- python manage.py check_duplicate_questions
- python manage.py award_badges
"""