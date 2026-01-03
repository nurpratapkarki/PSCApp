
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.utils import timezone
import json
from .mocktest_model import MockTest
from .question_answer_model import Question
class MockTestQuestion(models.Model):
    """
    Junction table linking MockTest and Question
    Tracks question order and marks allocation
    """
    mock_test = models.ForeignKey(
        MockTest,
        on_delete=models.CASCADE,
        related_name='test_questions'
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.PROTECT,
        related_name='mock_test_appearances'
    )
    question_order = models.IntegerField(
        help_text="Sequence number in the test"
    )
    marks_allocated = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=1.0,
        help_text="Marks for this question in this test"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'mock_test_questions'
        verbose_name = 'Mock Test Question'
        verbose_name_plural = 'Mock Test Questions'
        unique_together = [
            ['mock_test', 'question'],
            ['mock_test', 'question_order']
        ]
        ordering = ['mock_test', 'question_order']
    
    def __str__(self):
        return f"{self.mock_test.title_en} - Q{self.question_order}"

