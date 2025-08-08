from import_export import resources
from .models import ProjectEntry

class ProjectEntryResource(resources.ModelResource):
    class Meta:
        model = ProjectEntry
        import_id_fields = ['proj_name']
