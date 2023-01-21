from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, View, CreateView

from .models import Movie
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


# class JsonFilterMoviewsView(ListView):
#     def get_queryset(self):
#         queryset = Movie.objects.filter(
#             Q(year__in=self.request.GET.getlist('year')) |
#             Q(genres__in=self.request.GET.getlist('genre'))
#         ).distinct().values('title', 'tagline', 'url', 'poster')
#
#         return queryset
#
#     def get(self, request, *args, **kwargs):
#         queryset = list(self.get_queryset())
#         return JsonResponse({'movies': queryset}, safe=False)
