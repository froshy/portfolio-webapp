from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser 

from .models import ProjectEntry
from .serializers import ProjectEntrySerializer

@csrf_exempt
def project_entry_list(request):
    """
    List all project entries or create new project entry
    """

    # GET method is for reading from the database
    if request.method == "GET":
        project_entries = ProjectEntry.objects.all()
        serializer = ProjectEntrySerializer(project_entries, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    # POST method is for modifying the database
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ProjectEntrySerializer(data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def project_entry_detail(request, slug):
    """
    Retrieve, update, or delete a project entry
    """
    try:
        project_entry = ProjectEntry.objects.get(slug=slug)
    except ProjectEntry.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = ProjectEntrySerializer(project_entry)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = ProjectEntrySerializer(project_entry, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, staus=400)
    
    elif request.method == "DELETE":
        project_entry.delete()
        return HttpResponse(status=204)
    

        
