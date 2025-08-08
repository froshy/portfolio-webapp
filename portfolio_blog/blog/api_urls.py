from django.urls import path, include
from .api_views import blog_entry_list, blog_entry_detail 
urlpatterns = [
        path('blog_entry', blog_entry_list),
        path('blog_entry/<slug:slug>', blog_entry_detail),
        ]

