from django.contrib import admin
from .models import Movie, Actor, Filmmaker, Produser, Genere


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('film_name', 'premiere', 'date', 'date_ad')  
    search_fields = ('film_name', 'summary')  
    list_filter = ('premiere', 'genere', 'actor', 'filmmaker', 'produser')  
    prepopulated_fields = {'slug': ('film_name',)} 
    filter_horizontal = ('genere', 'actor', 'filmmaker', 'produser')  


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_of_birth', 'age')
    search_fields = ('name',)
    


@admin.register(Filmmaker)
class FilmmakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_of_birth', 'age')
    search_fields = ('name',)
    


@admin.register(Produser)
class ProduserAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_of_birth', 'age')
    search_fields = ('name',)
    


@admin.register(Genere)
class GenereAdmin(admin.ModelAdmin):
    list_display = ('genere_name',)
    search_fields = ('genere_name',)
    