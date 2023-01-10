from django.shortcuts import render
from django.views.generic import ListView

from .models import Movie


class MoviesView(ListView):
    model = Movie
    template = 'movies/movies_view_list.html'

