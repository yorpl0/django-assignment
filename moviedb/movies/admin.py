from django.contrib import admin
from .models import Movie
# Register your models here.
admin.site.register(Movie)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'release_date', 'genre')
    search_fields = ('title', 'director', 'genre')
