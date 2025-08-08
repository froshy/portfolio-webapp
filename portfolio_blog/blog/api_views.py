from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser 

from .models import BlogEntry 
from .serializers import BlogEntrySerializer
@csrf_exempt
def blog_entry_list(request):
    """
    List all blog entries or create new blog entry
    """

    # GET method is for reading from the database
    if request.method == "GET":
        blog_entries = BlogEntry.objects.all()
        serializer = BlogEntrySerializer(blog_entries, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    # POST method is for modifying the database
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = BlogEntrySerializer(data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def blog_entry_detail(request, slug):
    """
    Retrieve, update, or delete a blog entry
    """
    try:
        blog_entry = BlogEntry.objects.get(slug=slug)
    except BlogEntry.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = BlogEntrySerializer(blog_entry)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = BlogEntrySerializer(blog_entry, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, staus=400)
    
    elif request.method == "DELETE":
        blog_entry.delete()
        return HttpResponse(status=204)
    

        
