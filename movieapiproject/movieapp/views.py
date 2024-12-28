from . serializers import MovieListSerializer, MovieDetailSerializer
from rest_framework import generics, status
from . models import Movie
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from django.shortcuts import render
# Create your views here.

class MovieList(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer


class MovieSearchView(APIView):
    """API to search for movies by title."""

    def get(self, request):
        title = request.query_params.get("Title")
        if not title:
            return Response(
                {"error": "The 'title' query parameter is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        params = {
            "apikey": settings.OMDB_API_KEY,
            "s": title  
        }
        response = requests.get(settings.OMDB_BASE_URL, params=params)

        if response.status_code == 200:
            data = response.json()
            if data.get("Response") == "True":
                results = [
                    {
                        "Title": movie["Title"],
                        "Year": movie["Year"],
                        "imdbID": movie["imdbID"],
                        "Type": movie["Type"],
                        "Poster": movie.get("Poster", "N/A"),
                
                        
                    }
                    for movie in data.get("Search", [])
                ]
                return Response(results, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"error": data.get("Error", "No movies found.")},
                    status=status.HTTP_404_NOT_FOUND
                )
        return Response(
            {"error": "Failed to connect to OMDb API."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    
class AddMovie(generics.CreateAPIView):
    model = Movie
    serializer_class = MovieDetailSerializer

class UpdateMovie(generics.RetrieveUpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer
    lookup_field = 'id'

class DeleteMovie(generics.RetrieveDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer
    lookup_field = 'id'

class MovieDetailView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer
    lookup_field = 'id'

class FavouritedMovies(generics.ListAPIView):
    queryset = Movie.objects.filter(Favourite=True)
    serializer_class = MovieDetailSerializer