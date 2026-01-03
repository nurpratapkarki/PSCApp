from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.utils import timezone
import json

# ============================================================================
# QUESTION QUALITY CONTROL
# ============================================================================


class QuestionReport(models.Model):
    """
    Community-driven quality control for questions
    Users can report issues with questions
    """
    REASON_CHOICES = [
        ('INCORRECT_ANSWER', 'Incorrect Answer'),
        ('TYPO', 'Typo/Grammar Error'),
        ('INAPPROPRIATE', 'Inappropriate Content'),
        ('DUPLICATE', 'Duplicate Question'),
        ('OTHER', 'Other Issue'),
    ]
    
    STATUS_CHOICES = [
        ('PENDING', 'Pending Review'),
        ('UNDER_REVIEW', 'Under Review'),
        ('RESOLVED', 'Resolved'),
        ('REJECTED', 'Rejected'),
    ]
    
    question = models.ForeignKey(
        'Question',
        on_delete=models.CASCADE,
        related_name='reports'
    )
    reported_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='filed_reports'
    )
    reason = models.CharField(
        max_length=30,
        choices=REASON_CHOICES
    )
    description = models.TextField(
        help_text="Detailed explanation of the issue"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )
    reviewed_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='reviewed_reports',
        help_text="Admin or moderator who reviewed this report"
    )
    admin_notes = models.TextField(
        null=True,
        blank=True,
        help_text="Internal notes about resolution"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text="When the report was resolved"
    )
    
    class Meta:
        db_table = 'question_reports'
        verbose_name = 'Question Report'
        verbose_name_plural = 'Question Reports'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['question', 'status']),
            models.Index(fields=['status', 'created_at']),
            models.Index(fields=['reported_by']),
        ]
    
    def __str__(self):
        return f"Report #{self.id} - Q{self.question.id} ({self.get_reason_display()})"
    
    # TODO: Add method to mark as resolved
    # def resolve_report(self, admin_user, notes):
    #     pass
    
    # TODO: Add method to notify question creator
    # def notify_creator(self):
    #     pass
    
    # TODO: Add method to check if question has multiple reports
    # @staticmethod
    # def get_high_priority_questions():
    #     pass

