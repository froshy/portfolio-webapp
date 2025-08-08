from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
import datetime

class BlogEntry(models.Model):
    
    blog_title = models.CharField(primary_key=True, max_length=50, verbose_name="Blog Title")
    date_time = models.DateTimeField(default=timezone.now, verbose_name="Date & Time")
    content = models.TextField()
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.blog_title)
        super().save(*args, **kwargs)

