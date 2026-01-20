from rest_framework import serializers
from movie.models import Movie, Genere

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('__all__')

class PersenSerializers(serializers.Serializer):
    avatar = serializers.FileField
    name = serializers.CharField
    year_of_birth = serializers.DateField

class GenereSerializers(serializers.ModelSerializer):
    model = Genere
    fields = ('__all__')
