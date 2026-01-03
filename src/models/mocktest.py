from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.text import slugify

from src.models.branch import Branch, SubBranch
from src.models.question_answer import Question


class MockTest(models.Model):
    """
    Pre-configured or custom mock tests
    Can use standard timing or allow custom duration
    """

    TEST_TYPE_CHOICES = [
        ("OFFICIAL", "Official PSC Pattern"),
        ("COMMUNITY", "Community Created"),
        ("CUSTOM", "User Custom Test"),
    ]

    title_en = models.CharField(max_length=255)
    title_np = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description_en = models.TextField(null=True, blank=True)
    description_np = models.TextField(null=True, blank=True)
    test_type = models.CharField(
        max_length=20, choices=TEST_TYPE_CHOICES, default="COMMUNITY"
    )
    branch = models.ForeignKey(
        Branch, on_delete=models.PROTECT, related_name="mock_tests"
    )
    sub_branch = models.ForeignKey(
        SubBranch,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="mock_tests",
        help_text="Optional for branch-only tests",
    )
    total_questions = models.IntegerField(help_text="Total number of questions in test")
    duration_minutes = models.IntegerField(
        null=True, blank=True, help_text="If null, user can set their own timing"
    )
    use_standard_duration = models.BooleanField(
        default=True, help_text="Use TimeConfiguration or custom timing"
    )
    pass_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=40.0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_mock_tests",
        help_text="null for official tests",
    )
    is_public = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    attempt_count = models.IntegerField(
        default=0, help_text="Total attempts by all users"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "mock_tests"
        verbose_name = "Mock Test"
        verbose_name_plural = "Mock Tests"
        indexes = [
            models.Index(fields=["branch", "sub_branch", "is_public"]),
            models.Index(fields=["test_type", "is_active"]),
        ]

    def __str__(self):
        return f"{self.title_en} ({self.get_test_type_display()})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title_en)
        super().save(*args, **kwargs)

    # TODO: Add method to auto-generate test from question pool
    # def generate_from_categories(self, category_distribution):
    #     pass

    # TODO: Add method to get average score
    # def get_average_score(self):
    #     pass

    # TODO: Add method to get completion rate
    # def get_completion_rate(self):
    #     pass


class MockTestQuestion(models.Model):
    """
    Junction table linking MockTest and Question
    Tracks question order and marks allocation
    """

    mock_test = models.ForeignKey(
        MockTest, on_delete=models.CASCADE, related_name="test_questions"
    )
    question = models.ForeignKey(
        Question, on_delete=models.PROTECT, related_name="mock_test_appearances"
    )
    question_order = models.IntegerField(help_text="Sequence number in the test")
    marks_allocated = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=1.0,
        help_text="Marks for this question in this test",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "mock_test_questions"
        verbose_name = "Mock Test Question"
        verbose_name_plural = "Mock Test Questions"
        unique_together = [["mock_test", "question"], ["mock_test", "question_order"]]
        ordering = ["mock_test", "question_order"]

    def __str__(self):
        return f"{self.mock_test.title_en} - Q{self.question_order}"
