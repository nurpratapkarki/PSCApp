from django.db import models
from .user_model import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.utils import timezone
import json

class UserStatistics(models.Model):
    """
    Individual user achievement tracking
    Displays on user profile and personal dashboard
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='statistics'
    )
    questions_contributed = models.IntegerField(
        default=0,
        help_text="Lifetime contributions"
    )
    questions_made_public = models.IntegerField(
        default=0,
        help_text="Approved contributions"
    )
    questions_answered = models.IntegerField(
        default=0,
        help_text="Total questions attempted (practice + tests)"
    )
    correct_answers = models.IntegerField(
        default=0,
        help_text="Total correct answers"
    )
    mock_tests_completed = models.IntegerField(
        default=0,
        help_text="Number of completed mock tests"
    )
    study_streak_days = models.IntegerField(
        default=0,
        help_text="Current consecutive days active"
    )
    longest_streak = models.IntegerField(
        default=0,
        help_text="Personal best streak"
    )
    last_activity_date = models.DateField(
        null=True,
        blank=True,
        help_text="Last date user was active"
    )
    badges_earned = models.JSONField(
        default=dict,
        help_text="Dictionary of achievement badges"
    )
    contribution_rank = models.IntegerField(
        null=True,
        blank=True,
        help_text="Rank among all contributors"
    )
    accuracy_rank = models.IntegerField(
        null=True,
        blank=True,
        help_text="Rank by overall accuracy"
    )
    last_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'user_statistics'
        verbose_name = 'User Statistics'
        verbose_name_plural = 'User Statistics'
        indexes = [
            models.Index(fields=['contribution_rank']),
            models.Index(fields=['accuracy_rank']),
            models.Index(fields=['study_streak_days']),
        ]
    
    def __str__(self):
        return f"{self.user.username} Stats"
    
    # TODO: Add method to update streak (call daily)
    # def update_streak(self):
    #     pass
    
    # TODO: Add method to check and award badges
    # def check_badge_eligibility(self):
    #     pass
    
    # TODO: Add method to calculate accuracy percentage
    # def get_accuracy_percentage(self):
    #     pass
    
    # TODO: Add method to get all earned badge details
    # def get_badges_list(self):
    #     pass

