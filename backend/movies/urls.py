from django.urls import path

from .views import MovieListView, MovieDetailView

urlpatterns = [
    path('', MovieListView.as_view(), name='home'),
    path('<str:slug>/', MovieDetailView.as_view(), name='detail')
]
