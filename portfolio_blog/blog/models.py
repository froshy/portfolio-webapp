from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

import datetime

from .choices import CategoryChoices 

class Category(models.Model):
    name = models.CharField(unique=True, max_length=20, choices=CategoryChoices)
    slug = models.SlugField(unique=True, blank=True, default="")

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class BlogEntry(models.Model):
    
    title = models.CharField(primary_key=True, max_length=50, verbose_name="Blog Title")
    date_time = models.DateTimeField(default=timezone.now, verbose_name="Date & Time")
    content = models.TextField()
    category = models.ForeignKey(
            Category,
            on_delete=models.CASCADE,
            related_name="blogs",
            )
    slug = models.SlugField(null=False, blank=True,unique=True)


    class Meta:
        verbose_name_plural = "Blog Entries"

    def get_absolute_url(self):
        return reverse('detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
