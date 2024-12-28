from django.urls import path
from . views import MovieList, MovieSearchView, MovieDetailView, AddMovie, DeleteMovie,FavouritedMovies, UpdateMovie

urlpatterns = [
    path('',MovieList.as_view(),name='movielist'),
    path("search/", MovieSearchView.as_view(), name="movie-search"),
    path('movie/<int:id>/', MovieDetailView.as_view(), name='movie-detail'),

    path('addmovie',AddMovie.as_view()),
    path('deletemovie/<int:id>',DeleteMovie.as_view()),
    path('updatemovie/<int:id>',UpdateMovie.as_view()),

    path('favourites', FavouritedMovies.as_view(), name='favorite-movies'),

]
