from django.views.generic import ListView, DetailView

from .models import Movie


class MovieListView(ListView):
    model = Movie

    def get_queryset(self):
        return Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
    model = Movie
