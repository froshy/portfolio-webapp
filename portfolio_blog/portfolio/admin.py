from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import ProjectEntry 
# Register your models here.

class ProjectEntryResource(resources.ModelResource):
    class Meta:
        model = ProjectEntry
        import_id_fields = ['proj_name']

@admin.register(ProjectEntry)
class ProjectEntryAdmin(ImportExportModelAdmin):
    resource_classes=[ProjectEntryResource]
