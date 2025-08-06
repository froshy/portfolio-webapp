from django.db.models import Q

from django_filters import FilterSet, CharFilter
from .models import ProjectEntry


class ProjectEntryFilter(FilterSet):
    search = CharFilter(method='filter_search', label="Search")
    class Meta:
        model  = ProjectEntry
        fields = {
                'proj_name':['contains'],
                'description': ['contains']
                }
        exclude = ['slug']

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(proj_name__icontains=value) |
            Q(description__icontains=value) |
            Q(git_repo__icontains=value)
            )
