from django.urls import path, include

from rest_framework.routers import DefaultRouter 

from .api import FilmHomeViewSet, ActorViwset, ProduserViwset, FilmmakerViwset, GenereViwset


router = DefaultRouter()
router.register(r'movies', FilmHomeViewSet, basename='movies')
router.register(r'actors', ActorViwset, basename='actors')
router.register(r'producers', ProduserViwset, basename='producers')
router.register(r'filmmakers', FilmmakerViwset, basename='filmmakers')
router.register(r'genres', GenereViwset, basename='genres')

urlpatterns = router.urls
