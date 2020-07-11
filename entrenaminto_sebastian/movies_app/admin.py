from django.contrib import admin
from entrenaminto_sebastian.movies_app.models import Movie, Year
# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'director')
    search_fields = ['nombre']

@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    pass