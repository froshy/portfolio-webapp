from rest_framework import serializers
from .models import ProjectEntry


class ProjectEntrySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProjectEntry
        exclude = ['slug']

