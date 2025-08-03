from django_filters import FilterSet
from .models import ProjectEntry

class ProjectEntryFilter(FilterSet):
    class Meta:
        model  = ProjectEntry
        fields = {
                'proj_name':['contains'],
                'description': ['contains']
                }
        exclude = ['slug']


