from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters
from api.models import Project
from api.serializers import ProjectSerializer
# Create your views here.
class ProjectView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['id']
