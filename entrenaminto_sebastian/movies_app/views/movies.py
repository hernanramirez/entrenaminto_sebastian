# store/views.py
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# specific to this view
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse_lazy
from braces.views import LoginRequiredMixin
from entrenaminto_sebastian.movies_app.models import Movie

class MoviesListView(ListView):
    model = Movie
    template_name = 'movies_app/list.html'
    context_object_name = 'movies'
    paginate_by = 5

class MoviesCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    template_name = 'movies_app/forms.html'
    fields = ('nombre', 'año', 'director', 'poster')
    success_url = reverse_lazy('movies_app:movies-list')

class MoviesDetailView(DetailView):
    model = Movie
    template_name = 'movies_app/detail.html'
    context_object_name = 'movie'

class MoviesUpdateView(LoginRequiredMixin, UpdateView):
    model = Movie
    template_name = 'movies_app/forms.html'
    context_object_name = 'movie'
    fields = ('nombre', 'año', 'director', 'poster')

    def get_success_url(self):
        return reverse_lazy('movies_app:movies-list')

class MoviesDeleteView(LoginRequiredMixin, DeleteView):
    model = Movie
    context_object_name = 'movie'
    template_name = 'movies_app/confirm_delete.html'
    success_url = reverse_lazy('movies_app:movies-list')