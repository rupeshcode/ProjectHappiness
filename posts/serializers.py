from rest_framework import serializers
from .models import Story, Response, Blog


class StorySerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
#    owner = serializers.ReadOnlyField(source='owner.username')
#     published_date = serializers.DateTimeField(format="%Y-%m-%d")

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Story
        fields = '__all__'
#        read_only_fields = ('created',)


class ResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Response
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
#    owner = serializers.ReadOnlyField(source='owner.username')
#     published_date = serializers.DateTimeField(format="%Y-%m-%d")

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Blog
        fields = '__all__'
