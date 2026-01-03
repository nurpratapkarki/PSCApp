from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.utils import timezone
import json
from .user_model import User
class LeaderBoard(models.Model):
    """
    Tracks user rankings by time period, branch, and sub-branch
    Regenerated via scheduled cron jobs
    """
    TIME_PERIOD_CHOICES = [
        ('WEEKLY', 'Weekly'),
        ('MONTHLY', 'Monthly'),
        ('ALL_TIME', 'All Time'),
    ]
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='leaderboard_entries'
    )
    time_period = models.CharField(
        max_length=20,
        choices=TIME_PERIOD_CHOICES
    )
    branch = models.ForeignKey(
        'Branch',
        on_delete=models.CASCADE,
        related_name='leaderboard_entries'
    )
    sub_branch = models.ForeignKey(
        'SubBranch',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='leaderboard_entries',
        help_text="Leaderboard can be branch-wide or sub-branch specific"
    )
    rank = models.IntegerField(help_text="Current ranking position")
    total_score = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Sum of all test scores in this period"
    )
    tests_completed = models.IntegerField(
        default=0,
        help_text="Number of tests completed in this period"
    )
    accuracy_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text="Overall accuracy in this period"
    )
    last_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'leaderboards'
        verbose_name = 'LeaderBoard Entry'
        verbose_name_plural = 'LeaderBoard Entries'
        unique_together = [['user', 'time_period', 'branch', 'sub_branch']]
        ordering = ['time_period', 'branch', 'rank']
        indexes = [
            models.Index(fields=['time_period', 'branch', 'rank']),
            models.Index(fields=['user', 'time_period']),
        ]
    
    def __str__(self):
        return f"#{self.rank} - {self.user.username} ({self.get_time_period_display()})"
    
    # TODO: Add method to recalculate rankings for a time period
    # @staticmethod
    # def recalculate_rankings(time_period, branch=None, sub_branch=None):
    #     pass
    
    # TODO: Add method to get user's rank change from previous period
    # def get_rank_change(self):
    #     pass
    
    # TODO: Add method to get top N users
    # @staticmethod
    # def get_top_users(time_period, branch, limit=10):
    #     pass
