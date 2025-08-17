from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Category, ProjectEntry
from .resources import ProjectEntryResource

# Register your models here.


@admin.register(ProjectEntry)
class ProjectEntryAdmin(ImportExportModelAdmin):
    resource_classes = [ProjectEntryResource]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
