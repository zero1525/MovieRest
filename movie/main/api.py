from movie.models import *
from rest_framework import viewsets
from .serializers import MovieSerializer, PersenSerializers, GenereSerializers


class FilmHomeViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class BasePersonViewset(viewsets.ModelViewSet):
    serializer_class = PersenSerializers
    model = None

    def get_queryset(self):
        assert self.model is not None, 'model must be set'
        return self.model.objects.all()
    
class ActorViwset(BasePersonViewset):
    model = Actor

class ProduserViwset(BasePersonViewset):
    model = Produser

class FilmmakerViwset(BasePersonViewset):
    model = Filmmaker

class GenereViwset(viewsets.ModelViewSet):
    queryset = Genere.objects.all()
    serializer_class = GenereSerializers