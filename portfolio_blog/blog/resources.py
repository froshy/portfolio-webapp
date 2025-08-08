from .models import BlogEntry

from import_export import resources

class BlogEntryResource(resources.ModelResource):
    class Meta:
        model = BlogEntry
        import_id_fields = ['proj_name']
