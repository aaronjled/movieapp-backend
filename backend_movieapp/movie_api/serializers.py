from rest_framework import serializers 
from .models import Movie 

class MovieSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Movie # tell django which model to use
        fields = ('id', 'name', 'genre', 'raiting',) # tell django which fields to include