from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator 
from django.urls import reverse
import datetime

# Create your models here.
def current_year():
    return datetime.date.today().year    

class ProjectEntry(models.Model):

    proj_name = models.CharField(primary_key=True, max_length=50, verbose_name="Project Name")
    description = models.TextField(verbose_name="Description")
    start_year = models.IntegerField(null=False, verbose_name="Development Start Year",
                                     validators=[MinValueValidator(1900), MaxValueValidator(current_year)], help_text="Enter a year between 1900 and current year")
    git_repo = models.URLField(null=False, verbose_name="Github Repository")
    slug = models.SlugField(null=False, unique=True)

    def get_absolute_url(self):
        return reverse('detail', args=[self.slug])
