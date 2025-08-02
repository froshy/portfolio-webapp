from django.shortcuts import render
from django.http import HttpResponse

from django_tables2.views import SingleTableMixin
from django_filters.views import FilterView

from .models import ProjectEntry
from .tables import ProjectEntryTable
from .filters import ProjectEntryFilter
# Create your views here.

def index(request):
    return HttpResponse("Hello, you are at index")

class Index(SingleTableMixin, FilterView):
    table_class = ProjectEntryTable
    model = ProjectEntry
    template_name = 'index.html'
