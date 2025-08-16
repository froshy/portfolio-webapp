import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


###################
# Default Helpers #
###################
def category_default():
    obj, _ = Category.objects.get_or_create(name="General")
    return obj


# Create your models here.
def current_year():
    return datetime.date.today().year


class Category(models.Model):
    name = models.CharField(unique=True)

    def __str__(self):
        return self.name


class ProjectEntry(models.Model):
    proj_name = models.CharField(
        primary_key=True, max_length=50, verbose_name="Project Name"
    )
    category = models.ForeignKey(Category, default=category_default)
    description = models.TextField(verbose_name="Description")
    start_year = models.IntegerField(
        null=False,
        verbose_name="Development Start Year",
        validators=[MinValueValidator(1900), MaxValueValidator(current_year)],
        help_text="Enter a year between 1900 and current year",
    )
    git_repo = models.URLField(null=False, verbose_name="Github Repository")
    slug = models.SlugField(null=False, blank=True, unique=True)

    class Meta:
        verbose_name_plural = "Project Entries"

    def get_absolute_url(self):
        return reverse("detail", args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.proj_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.proj_name)
