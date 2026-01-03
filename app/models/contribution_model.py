
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.utils import timezone
import json
from question_answer_model import Question

from .user_model import User

class Contribution(models.Model):
    """
    Tracks user-contributed questions through approval process
    Monthly recognition and Facebook shoutouts
    """
    STATUS_CHOICES = [
        ('PENDING', 'Pending Approval'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
        ('MADE_PUBLIC', 'Made Public'),
    ]
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='contributions'
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='contribution_records'
    )
    contribution_month = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(12)],
        help_text="Month of contribution (1-12)"
    )
    contribution_year = models.IntegerField(
        help_text="Year of contribution"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )
    is_featured = models.BooleanField(
        default=False,
        help_text="Selected for Facebook shoutout"
    )
    approval_date = models.DateTimeField(
        null=True,
        blank=True,
        help_text="When the contribution was approved"
    )
    public_date = models.DateTimeField(
        null=True,
        blank=True,
        help_text="When made available to all users"
    )
    rejection_reason = models.TextField(
        null=True,
        blank=True,
        help_text="If rejected, explanation why"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'contributions'
        verbose_name = 'Contribution'
        verbose_name_plural = 'Contributions'
        unique_together = [['user', 'question']]
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', 'status']),
            models.Index(fields=['contribution_year', 'contribution_month']),
            models.Index(fields=['status', 'is_featured']),
        ]
    
    def __str__(self):
        return f"{self.user.username} - Q{self.question.id} ({self.status})"
    
    # TODO: Add method to approve contribution
    # def approve_contribution(self):
    #     pass
    
    # TODO: Add method to reject with reason
    # def reject_contribution(self, reason):
    #     pass
    
    # TODO: Add method to make public (monthly batch)
    # def make_public(self):
    #     pass
    
    # TODO: Add method to select for Facebook feature
    # def feature_for_social(self):
    #     pass
    
    # TODO: Get top contributors for a month
    # @staticmethod
    # def get_top_contributors(year, month, limit=10):
    #     pass

