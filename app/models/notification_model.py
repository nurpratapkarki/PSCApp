from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.utils import timezone
import json
from .user_model import User
class Notification(models.Model):
    """
    User alerts for contributions, leaderboard changes, etc.
    Keeps users engaged with the platform
    """
    TYPE_CHOICES = [
        ('CONTRIBUTION_APPROVED', 'Contribution Approved'),
        ('QUESTION_PUBLIC', 'Question Made Public'),
        ('LEADERBOARD_RANK', 'Leaderboard Rank Change'),
        ('REPORT_RESOLVED', 'Report Resolved'),
        ('STREAK_ALERT', 'Streak Alert'),
        ('MILESTONE', 'Milestone Achieved'),
        ('GENERAL', 'General Notification'),
    ]
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notifications'
    )
    notification_type = models.CharField(
        max_length=30,
        choices=TYPE_CHOICES
    )
    title_en = models.CharField(
        max_length=255,
        help_text="Notification heading in English"
    )
    title_np = models.CharField(
        max_length=255,
        help_text="Notification heading in Nepali"
    )
    message_en = models.TextField(help_text="Notification body in English")
    message_np = models.TextField(help_text="Notification body in Nepali")
    related_question = models.ForeignKey(
        'Question',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='notifications',
        help_text="If notification is about a specific question"
    )
    related_mock_test = models.ForeignKey(
        'MockTest',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='notifications'
    )
    is_read = models.BooleanField(default=False)
    action_url = models.CharField(
        max_length=500,
        null=True,
        blank=True,
        help_text="Deep link for mobile app navigation"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'notifications'
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', 'is_read']),
            models.Index(fields=['user', 'notification_type']),
            models.Index(fields=['created_at']),
        ]
    
    def __str__(self):
        return f"{self.user.username} - {self.title_en}"
    
    # TODO: Add method to mark as read
    # def mark_as_read(self):
    #     pass
    
    # TODO: Add method to create notification for multiple users
    # @staticmethod
    # def create_bulk_notifications(users, notification_type, title, message):
    #     pass
    
    # TODO: Add method to get unread count for user
    # @staticmethod
    # def get_unread_count(user):
    #     pass
