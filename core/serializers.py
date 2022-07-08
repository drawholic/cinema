from rest_framework.serializers import ModelSerializer
from .models import Movie, Actor, Reservation
from django.contrib.auth.models import User


class ActorSerializer(ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'


class MovieSerializer(ModelSerializer):
    actors = ActorSerializer(source='cast', many=True, read_only=True)

    class Meta:
        model = Movie
        exclude = ['cast']


class ReservationSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


class UserMovies(ModelSerializer):
    reservations = ReservationSerializer(source='customer_set', many=True, read_only=True)

    class Meta:
        model = User
        fields = ['reservations', 'username']