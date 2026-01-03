from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.utils import timezone
import json

class Branch(models.Model):
    """
    Main examination branches (e.g., Nasu, Kharidar, Engineering, Technical)
    Some branches have sub-branches, others don't
    """
    name_en = models.CharField(
        max_length=255, 
        unique=True,
        help_text="Branch name in English"
    )
    name_np = models.CharField(
        max_length=255,
        help_text="Branch name in Nepali"
    )
    slug = models.SlugField(max_length=255, unique=True)
    description_en = models.TextField(null=True, blank=True)
    description_np = models.TextField(null=True, blank=True)
    icon = models.ImageField(
        upload_to='branch_icons/', 
        null=True, 
        blank=True
    )
    has_sub_branches = models.BooleanField(
        default=False,
        help_text="Does this branch have specializations?"
    )
    display_order = models.IntegerField(
        default=0,
        help_text="Order for displaying in UI"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'branches'
        verbose_name = 'Branch'
        verbose_name_plural = 'Branches'
        ordering = ['display_order', 'name_en']
    
    def __str__(self):
        return self.name_en
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name_en)
        super().save(*args, **kwargs)
    
    # TODO: Add method to get all active sub-branches
    # def get_sub_branches(self):
    #     pass
    
    # TODO: Add method to get total questions for this branch
    # def get_total_questions(self):
    #     pass
    
    # TODO: Add method to get active users targeting this branch
    # def get_active_users_count(self):
    #     pass

