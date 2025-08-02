from django.db import models

# Create your models here.

class ProjectEntry(models.Model):

    proj_name = models.CharField(primary_key=True, max_length=50, verbose_name="Project Name")
    description = models.TextField(verbose_name="Description")
    start_year = models.IntegerField(null=False, verbose_name="Development Start Year")
    git_repo = models.URLField(null=False, verbose_name="Github Repository")

