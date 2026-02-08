from rest_framework import serializers
from .models import Movies

class MovieSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Movies
        fields = '__all__'
