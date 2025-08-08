from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .resources import ProjectEntryResource
from .models import ProjectEntry 
# Register your models here.


@admin.register(ProjectEntry)
class ProjectEntryAdmin(ImportExportModelAdmin):
    resource_classes=[ProjectEntryResource]
