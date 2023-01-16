from django.urls import path

from .views import MovieListView, MovieDetailView, ReviewCreateView

urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),
    path('review/<int:pk>', ReviewCreateView.as_view(), name='add_review'),
]
