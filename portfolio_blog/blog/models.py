from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

from .choices import CategoryChoices

###################
# DEFAULT HELPERS #
###################


def category_default():
    """
    Helper for setting category default.
    Used when Blog item is deleted and on_delete = SET_DEFAULT
    """
    category, _ = Category.objects.get_or_create(name="General")
    return category.pk


class Category(models.Model):
    """
    models.Model Category Object.
    Used as foreign key relation to BlogEntry
    """

    name = models.CharField(unique=True, max_length=20, choices=CategoryChoices)
    slug = models.SlugField(unique=True, blank=True, default="")

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        if self.name == "General":
            raise Exception("'General' category can not be deleted.")
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class BlogEntry(models.Model):
    """
    The BlogEntry models.Model object.
    ORM for BlogEntry table.
    """

    title = models.CharField(primary_key=True, max_length=50, verbose_name="Blog Title")
    date_time = models.DateTimeField(default=timezone.now, verbose_name="Date & Time")
    content = models.TextField()
    category = models.ForeignKey(
        Category,
        default=category_default,
        on_delete=models.SET_DEFAULT,
        related_name="blogs",
        verbose_name="Blog Category",
    )
    slug = models.SlugField(null=False, blank=True, unique=True)

    class Meta:
        verbose_name_plural = "Blog Entries"

    def get_absolute_url(self):
        return reverse("detail", args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
