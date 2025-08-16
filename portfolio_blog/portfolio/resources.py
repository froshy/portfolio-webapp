from django.core.exceptions import ObjectDoesNotExist
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget

from .models import ProjectEntry


class AutoForeignKeyWidget(ForeignKeyWidget):
    def clean(self, value, row=None, **kwargs):
        try:
            return super().clean(value, row, **kwargs)
        except ObjectDoesNotExist:
            obj, _ = self.model.objects.get_or_create(**{self.field: "name"})
            return obj


class ProjectEntryResource(resources.ModelResource):
    catalog = fields.Field(widget=ForeignKeyWidget)

    class Meta:
        model = ProjectEntry
        import_id_fields = ["proj_name"]
