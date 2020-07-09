from django.contrib import admin
from entrenaminto_sebastian.telefonera_app.models import Telefono

@admin.register(Telefono)
class TelefonoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'nombre', 'telefono')
    search_fields = ['nombre']
    #inlines = [CatalogoInline]
