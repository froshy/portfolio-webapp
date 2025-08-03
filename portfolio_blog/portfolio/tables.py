from django_tables2 import tables
from .models import ProjectEntry

class ProjectEntryTable(tables.Table):
    proj_name = tables.Column(linkify=True)
    class Meta:
        model = ProjectEntry
        template_name = 'django_tables2/bootstrap.html'
        exclude = ['slug']

