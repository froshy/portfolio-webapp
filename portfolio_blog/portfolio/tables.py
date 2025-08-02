from django_tables2 import tables
from .models import ProjectEntry

class ProjectEntryTable(tables.Table):
    class Meta:
        model = ProjectEntry
        template_name = 'django_tables2/bootstrap.html'

