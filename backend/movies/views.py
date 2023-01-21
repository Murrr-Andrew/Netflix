from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, View, CreateView

from .models import Movie, Reviews, Category
from .forms import ReviewForm


class MovieListView(ListView):
    model = Movie

    def get_queryset(self):
        return Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
    model = Movie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReviewForm()
        return context


class ReviewCreateView(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)

        if form.is_valid():
            form = form.save(commit=False)

            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))

            form.movie = movie
            form.save()

        return redirect(movie.get_absolute_url())
