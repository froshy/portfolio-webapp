from rest_framework import serializers
from .models import BlogEntry 


class BlogEntrySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BlogEntry 
        exclude = ['slug']

