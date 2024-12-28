from rest_framework import serializers
from . models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','Title','YearOfRelease']

class MovieListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','Title','YearOfRelease','Favourite','url']
        extra_kwargs = {
            'url': {'view_name': 'movie-detail', 'lookup_field': 'id'}  # Ensure correct view_name
        }

class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

