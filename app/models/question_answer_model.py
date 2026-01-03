from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.utils import timezone
import json
from .category_model import Category
class Question(models.Model):
    """
    Individual exam questions with bilingual support
    Tracks contribution status and public availability
    """
    DIFFICULTY_CHOICES = [
        ('EASY', 'Easy'),
        ('MEDIUM', 'Medium'),
        ('HARD', 'Hard'),
    ]
    
    TYPE_CHOICES = [
        ('MCQ', 'Multiple Choice Question'),
        # Future: TRUE_FALSE, FILL_BLANK, etc.
    ]
    
    STATUS_CHOICES = [
        ('DRAFT', 'Draft'),
        ('PENDING_REVIEW', 'Pending Review'),
        ('PUBLIC', 'Public'),
        ('PRIVATE', 'Private'),
    ]
    
    question_text_en = models.TextField(help_text="Question in English")
    question_text_np = models.TextField(help_text="Question in Nepali")
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='questions',
        help_text="Single category assignment"
    )
    difficulty_level = models.CharField(
        max_length=10,
        choices=DIFFICULTY_CHOICES,
        null=True,
        blank=True,
        help_text="Required only for IQ & Mathematics categories"
    )
    question_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default='MCQ'
    )
    explanation_en = models.TextField(
        help_text="Detailed explanation for correct answer in English"
    )
    explanation_np = models.TextField(
        help_text="Detailed explanation in Nepali"
    )
    image = models.ImageField(
        upload_to='question_images/',
        null=True,
        blank=True,
        help_text="Optional diagram or chart"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='DRAFT'
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='contributed_questions',
        help_text="User who contributed this question"
    )
    is_public = models.BooleanField(default=False)
    consent_given = models.BooleanField(
        default=False,
        help_text="User agreed to make question public"
    )
    scheduled_public_date = models.DateField(
        null=True,
        blank=True,
        help_text="When question becomes public (monthly batch)"
    )
    source_reference = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="e.g., 'PSC 2078 Nasu Exam'"
    )
    times_attempted = models.IntegerField(
        default=0,
        help_text="How many times this question was attempted"
    )
    times_correct = models.IntegerField(
        default=0,
        help_text="How many times answered correctly"
    )
    reported_count = models.IntegerField(
        default=0,
        help_text="Number of quality reports filed"
    )
    is_verified = models.BooleanField(
        default=False,
        help_text="Admin verified quality"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'questions'
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        indexes = [
            models.Index(fields=['category', 'status']),
            models.Index(fields=['is_public', 'status']),
            models.Index(fields=['created_by', 'status']),
            models.Index(fields=['scheduled_public_date']),
        ]
    
    def __str__(self):
        return f"Q{self.id}: {self.question_text_en[:50]}..."
    
    # TODO: Add method to calculate accuracy rate
    # def get_accuracy_rate(self):
    #     pass
    
    # TODO: Add method to get all user attempts for this question
    # def get_attempt_history(self, user=None):
    #     pass
    
    # TODO: Add method to check if question has duplicate in public pool
    # def check_duplicate(self):
    #     pass
    
    # TODO: Add method to schedule for monthly publication
    # def schedule_publication(self, target_date):
    #     pass


class Answer(models.Model):
    """
    Answer options for MCQ questions
    One question has multiple answers, only one is correct
    """
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='answers'
    )
    answer_text_en = models.TextField(help_text="Answer option in English")
    answer_text_np = models.TextField(help_text="Answer option in Nepali")
    is_correct = models.BooleanField(
        default=False,
        help_text="Only one answer should be True per question"
    )
    display_order = models.IntegerField(
        default=0,
        help_text="Order for A, B, C, D display"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'answers'
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
        ordering = ['question', 'display_order']
        unique_together = [['question', 'display_order']]
    
    def __str__(self):
        correct_mark = "✓" if self.is_correct else "✗"
        return f"{correct_mark} {self.answer_text_en[:30]}..."
    
    # TODO: Add validation to ensure only one correct answer per question
    # def clean(self):
    #     pass

