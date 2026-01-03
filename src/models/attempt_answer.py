from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from src.models.mocktest import MockTest
from src.models.question_answer import Answer, Question


class UserAttempt(models.Model):
    """
    Tracks individual test/practice sessions
    Records timing, score, and completion status
    """

    STATUS_CHOICES = [
        ("IN_PROGRESS", "In Progress"),
        ("COMPLETED", "Completed"),
        ("ABANDONED", "Abandoned"),
    ]

    MODE_CHOICES = [
        ("MOCK_TEST", "Mock Test"),
        ("PRACTICE", "Practice Mode"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="attempts")
    mock_test = models.ForeignKey(
        MockTest,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="user_attempts",
        help_text="null for practice mode",
    )
    start_time = models.DateTimeField(
        default=timezone.now, help_text="When user started the attempt"
    )
    end_time = models.DateTimeField(
        null=True, blank=True, help_text="When completed/submitted"
    )
    total_time_taken = models.IntegerField(
        null=True,
        blank=True,
        help_text="Total seconds spent (calculated on completion)",
    )
    score_obtained = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    total_score = models.DecimalField(
        max_digits=7, decimal_places=2, help_text="Maximum possible score"
    )
    percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Calculated on completion",
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="IN_PROGRESS"
    )
    mode = models.CharField(max_length=20, choices=MODE_CHOICES, default="MOCK_TEST")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user_attempts"
        verbose_name = "User Attempt"
        verbose_name_plural = "User Attempts"
        indexes = [
            models.Index(fields=["user", "status"]),
            models.Index(fields=["mock_test", "status"]),
            models.Index(fields=["created_at"]),
        ]

    def __str__(self):
        test_name = self.mock_test.title_en if self.mock_test else "Practice"
        return f"{self.user.username} - {test_name} ({self.status})"

    # TODO: Add method to calculate final score and percentage
    # def calculate_results(self):
    #     pass

    # TODO: Add method to mark as completed
    # def complete_attempt(self):
    #     pass

    # TODO: Add method to get time remaining (for timed tests)
    # def get_time_remaining(self):
    #     pass


class UserAnswer(models.Model):
    """
    Individual question responses within an attempt
    Tracks selected answer, correctness, and time taken
    """

    user_attempt = models.ForeignKey(
        UserAttempt, on_delete=models.CASCADE, related_name="user_answers"
    )
    question = models.ForeignKey(
        Question, on_delete=models.PROTECT, related_name="user_responses"
    )
    selected_answer = models.ForeignKey(
        Answer,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="user_selections",
        help_text="null if question was skipped",
    )
    is_correct = models.BooleanField(default=False)
    time_taken_seconds = models.IntegerField(
        null=True, blank=True, help_text="Time spent on this specific question"
    )
    is_skipped = models.BooleanField(default=False)
    is_marked_for_review = models.BooleanField(
        default=False, help_text="User flagged to revisit later"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True, help_text="Updated when user changes answer"
    )

    class Meta:
        db_table = "user_answers"
        verbose_name = "User Answer"
        verbose_name_plural = "User Answers"
        unique_together = [["user_attempt", "question"]]
        indexes = [
            models.Index(fields=["user_attempt", "is_correct"]),
            models.Index(fields=["question", "is_correct"]),
        ]

    def __str__(self):
        return f"Q{self.question.id} - {'Correct' if self.is_correct else 'Incorrect'}"

    def save(self, *args, **kwargs):
        # Auto-check correctness if answer is selected
        if self.selected_answer:
            self.is_correct = self.selected_answer.is_correct
            self.is_skipped = False
        else:
            self.is_skipped = True
            self.is_correct = False
        super().save(*args, **kwargs)
