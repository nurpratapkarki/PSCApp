from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.utils import timezone
import json
from .branch_model import Branch
class SubBranch(models.Model):
    """
    Specializations within branches (e.g., Civil Engineering, Electrical Engineering)
    Only exists for branches where has_sub_branches=True
    """
    branch = models.ForeignKey(
        Branch, 
        on_delete=models.CASCADE, 
        related_name='sub_branches'
    )
    name_en = models.CharField(max_length=255)
    name_np = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description_en = models.TextField(null=True, blank=True)
    description_np = models.TextField(null=True, blank=True)
    icon = models.ImageField(
        upload_to='subbranch_icons/', 
        null=True, 
        blank=True
    )
    display_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'sub_branches'
        verbose_name = 'Sub Branch'
        verbose_name_plural = 'Sub Branches'
        unique_together = [['branch', 'slug']]
        ordering = ['branch', 'display_order', 'name_en']
    
    def __str__(self):
        return f"{self.branch.name_en} - {self.name_en}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name_en)
        super().save(*args, **kwargs)
    
    # TODO: Add method to get total questions for this sub-branch
    # def get_total_questions(self):
    #     pass
