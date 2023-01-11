from django.views.generic import ListView, DetailView

from .models import Movie


class MovieListView(ListView):
    model = Movie
    template = 'movies/movie_list.html'

    def get_queryset(self):
        return Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'
