from django.contrib import admin
from entrenaminto_sebastian.movies_app.models import Movie

# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'año', 'director')
    search_fields = ['nombre']
