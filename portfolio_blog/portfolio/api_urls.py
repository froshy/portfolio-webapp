from django.urls import path, include
from .api_views import project_entry_list, project_entry_detail
urlpatterns = [
        path('project_entry', project_entry_list),
        path('project_entry/<slug:slug>', project_entry_detail),
        ]
