from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime

class BlogEntry(models.Model):
    
    blog_title = models.CharField(primary_key=True, max_length=50, verbose_name="Blog Title")
    date_time = models.DateTimeField(default=timezone.now, verbose_name="Date & Time")
    content = models.TextField()

