from rest_framework.serializers import ModelSerializer
from .models import Movie, Actor


class ActorSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class MovieSerializer(ModelSerializer):
    actors = ActorSerializer(source='cast', many=True, read_only=True)

    class Meta:
        model = Movie
        exclude = ['cast']
