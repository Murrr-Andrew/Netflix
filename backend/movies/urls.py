from django.urls import path

from .views import MovieListView, MovieDetailView

urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),
    path('<str:slug>/', MovieDetailView.as_view(), name='movie_detail')
]
