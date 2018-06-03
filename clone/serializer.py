from rest_framework import serializers
from .models import ImagePost

class ImagePostSerializer(serializers.ModelSerializer):
    '''
    Convert ImagePost model to JSON
    '''
    class Meta:
        model = ImagePost
        fields = ('id', 'name', 'image', 'tags')