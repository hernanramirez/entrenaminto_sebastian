from django.urls import path
from entrenaminto_sebastian.movies_app.views import movies

app_name = "movies_app"

urlpatterns = [
    path('', movies.MoviesListView.as_view(), name='movies-list'),
    path('create/', movies.MoviesCreateView.as_view(), name='movies-create'),
    path('detail/<int:pk>', movies.MoviesDetailView.as_view(), name='movies-detail'),
    path('update/<int:pk>', movies.MoviesUpdateView.as_view(), name='movies-update'),
    path('delete/<int:pk>', movies.MoviesDeleteView.as_view(), name='movies-delete'),
]