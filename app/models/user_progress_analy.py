from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.utils import timezone
import json
from .category_model import Category

class UserProgress(models.Model):
    """
    Tracks user performance per category
    Used for analytics and personalized recommendations
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='category_progress'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='user_progress'
    )
    questions_attempted = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)
    accuracy_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.0,
        help_text="Auto-calculated from correct/attempted ratio"
    )
    average_time_seconds = models.IntegerField(
        null=True,
        blank=True,
        help_text="Average time per question in this category"
    )
    last_attempted_date = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Last time user attempted question from this category"
    )
    weak_topics = models.JSONField(
        null=True,
        blank=True,
        help_text="JSON array of specific sub-topics user struggles with"
    )
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'user_progress'
        verbose_name = 'User Progress'
        verbose_name_plural = 'User Progress Records'
        unique_together = [['user', 'category']]
        indexes = [
            models.Index(fields=['user', 'accuracy_percentage']),
            models.Index(fields=['category', 'accuracy_percentage']),
        ]
    
    def __str__(self):
        return f"{self.user.username} - {self.category.name_en} ({self.accuracy_percentage}%)"
    
    # TODO: Add method to update progress after each attempt
    # def update_progress(self, is_correct, time_taken):
    #     pass
    
    # TODO: Add method to identify weak topics
    # def analyze_weak_topics(self):
    #     pass

class StudyCollection(models.Model):
    """
    User's personal question collections/playlists
    For organizing questions by topic, difficulty, or custom criteria
    """
    name = models.CharField(
        max_length=255,
        help_text="Collection name (e.g., 'My Weak Questions', 'Math Practice')"
    )
    description = models.TextField(
        null=True,
        blank=True,
        help_text="What this collection is for"
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='study_collections'
    )
    is_private = models.BooleanField(
        default=True,
        help_text="Personal vs shareable collections"
    )
    questions = models.ManyToManyField(
        'Question',
        related_name='study_collections',
        blank=True,
        help_text="User's curated question list"
    )
    icon = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        help_text="Icon identifier for UI"
    )
    color_code = models.CharField(
        max_length=7,
        null=True,
        blank=True,
        help_text="Hex color for UI (e.g., #FF5733)"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'study_collections'
        verbose_name = 'Study Collection'
        verbose_name_plural = 'Study Collections'
        ordering = ['-updated_at']
        indexes = [
            models.Index(fields=['created_by', 'is_private']),
        ]
    
    def __str__(self):
        return f"{self.name} by {self.created_by.username}"
    
    # TODO: Add method to get total questions in collection
    # def get_question_count(self):
    #     pass
    
    # TODO: Add method to add multiple questions at once
    # def add_questions(self, question_ids):
    #     pass
    
    # TODO: Add method to remove questions
    # def remove_questions(self, question_ids):
    #     pass
    
    # TODO: Add method to share collection with other users
    # def share_collection(self):
    #     pass
