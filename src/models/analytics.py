from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from src.models.question_answer import Question
from src.models.user import User as CustomUser


class Contribution(models.Model):
    """
    Tracks user-contributed questions through approval process
    Monthly recognition and Facebook shoutouts
    """

    STATUS_CHOICES = [
        ("PENDING", "Pending Approval"),
        ("APPROVED", "Approved"),
        ("REJECTED", "Rejected"),
        ("MADE_PUBLIC", "Made Public"),
    ]

    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="contributions"
    )
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="contribution_records"
    )
    contribution_month = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(12)],
        help_text="Month of contribution (1-12)",
    )
    contribution_year = models.IntegerField(help_text="Year of contribution")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")
    is_featured = models.BooleanField(
        default=False, help_text="Selected for Facebook shoutout"
    )
    approval_date = models.DateTimeField(
        null=True, blank=True, help_text="When the contribution was approved"
    )
    public_date = models.DateTimeField(
        null=True, blank=True, help_text="When made available to all users"
    )
    rejection_reason = models.TextField(
        null=True, blank=True, help_text="If rejected, explanation why"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "contributions"
        verbose_name = "Contribution"
        verbose_name_plural = "Contributions"
        unique_together = [["user", "question"]]
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["user", "status"]),
            models.Index(fields=["contribution_year", "contribution_month"]),
            models.Index(fields=["status", "is_featured"]),
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


class DailyActivity(models.Model):
    """
    Daily platform activity tracking for trend analysis
    Used for charts and growth metrics
    """

    date = models.DateField(unique=True, help_text="Date of activity tracking")
    new_users = models.IntegerField(default=0, help_text="New user registrations")
    questions_added = models.IntegerField(
        default=0, help_text="New questions added this day"
    )
    questions_approved = models.IntegerField(
        default=0, help_text="Questions approved by admins"
    )
    mock_tests_taken = models.IntegerField(
        default=0, help_text="Tests started this day"
    )
    total_answers_submitted = models.IntegerField(
        default=0, help_text="Question attempts across all users"
    )
    active_users = models.IntegerField(
        default=0, help_text="Unique users who performed any action"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "daily_activities"
        verbose_name = "Daily Activity"
        verbose_name_plural = "Daily Activities"
        ordering = ["-date"]
        indexes = [
            models.Index(fields=["date"]),
        ]

    def __str__(self):
        return f"Activity: {self.date}"

    # TODO: Add method to get activity for date range
    # @staticmethod
    # def get_activity_range(start_date, end_date):
    #     pass

    # TODO: Add method to get weekly/monthly trends
    # @staticmethod
    # def get_trend_data(period='week'):
    #     pass

    # TODO: Add scheduled task to create/update daily record
    # @staticmethod
    # def record_today_activity():
    #     pass


class LeaderBoard(models.Model):
    """
    Tracks user rankings by time period, branch, and sub-branch
    Regenerated via scheduled cron jobs
    """

    TIME_PERIOD_CHOICES = [
        ("WEEKLY", "Weekly"),
        ("MONTHLY", "Monthly"),
        ("ALL_TIME", "All Time"),
    ]

    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="leaderboard_entries"
    )
    time_period = models.CharField(max_length=20, choices=TIME_PERIOD_CHOICES)
    branch = models.ForeignKey(
        "Branch", on_delete=models.CASCADE, related_name="leaderboard_entries"
    )
    sub_branch = models.ForeignKey(
        "SubBranch",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="leaderboard_entries",
        help_text="Leaderboard can be branch-wide or sub-branch specific",
    )
    rank = models.IntegerField(help_text="Current ranking position")
    total_score = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Sum of all test scores in this period",
    )
    tests_completed = models.IntegerField(
        default=0, help_text="Number of tests completed in this period"
    )
    accuracy_percentage = models.DecimalField(
        max_digits=5, decimal_places=2, help_text="Overall accuracy in this period"
    )
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "leaderboards"
        verbose_name = "LeaderBoard Entry"
        verbose_name_plural = "LeaderBoard Entries"
        unique_together = [["user", "time_period", "branch", "sub_branch"]]
        ordering = ["time_period", "branch", "rank"]
        indexes = [
            models.Index(fields=["time_period", "branch", "rank"]),
            models.Index(fields=["user", "time_period"]),
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
