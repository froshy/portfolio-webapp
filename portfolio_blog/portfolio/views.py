from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView

from django_tables2.views import SingleTableMixin
from django_filters.views import FilterView

from .models import ProjectEntry
from .tables import ProjectEntryTable
from .filters import ProjectEntryFilter
# Create your views here.

class Index(SingleTableMixin, FilterView):
    table_class = ProjectEntryTable
    model = ProjectEntry
    template_name = 'portfolio/index.html'
    filterset_class = ProjectEntryFilter

    def get_paginate_by(self, *args, **kwargs):
        super().get_paginate_by(*args, **kwargs)

class Detail(DetailView):
    model = ProjectEntry
    template_name = 'portfolio/detail.html'
