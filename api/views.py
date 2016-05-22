from rest_framework import viewsets
from api.serializers import NameSerializer
from hello_world_app.models import Name


class NameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows names to be viewed.
    """
    queryset = Name.objects.all()
    serializer_class = NameSerializer
