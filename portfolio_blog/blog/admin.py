from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import BlogEntry, Category
from .resources import BlogEntryResource

# Register your models here.


@admin.register(BlogEntry)
class BlogEntryAdmin(ImportExportModelAdmin):
    resource_classes = [BlogEntryResource]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category

    def has_delete_permission(self, request, obj=None):
        if obj and obj.name == "General":
            return False
        return super().has_delete_permission(request, obj)
