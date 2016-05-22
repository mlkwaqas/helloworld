from rest_framework import serializers
from hello_world_app.models import Name


class NameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Name
        fields = ('value', 'created_at')
