from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import BlogEntry, Category
from .resources import BlogEntryResource
# Register your models here.


@admin.register(BlogEntry)
class BlogEntryAdmin(ImportExportModelAdmin):
    resource_classes=[BlogEntryResource]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
