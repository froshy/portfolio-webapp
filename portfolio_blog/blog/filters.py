from django.db.models import Q

from django_filters import FilterSet, CharFilter
from .models import BlogEntry 


class BlogEntryFilter(FilterSet):
    search = CharFilter(method='filter_search', label="Search")
    class Meta:
        model  = BlogEntry
        fields = {
                'blog_title':['contains'],
                'content': ['contains']
                }
        exclude = ['slug']

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(blog_title__icontains=value) |
            Q(content__icontains=value) 
            )
