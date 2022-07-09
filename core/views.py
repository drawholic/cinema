import rest_framework.permissions
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import Movie, Reservation, Actor
from .serializers import MovieSerializer, ReservationSerializer, UserMovies
from django.contrib.auth.models import User
from django.db import connection


class UserMoviesView(RetrieveAPIView):
    queryset = User
    serializer_class = UserMovies

    def get(self, request):
        user = self.queryset.objects.get(id=request.user.id)
        serializer = self.serializer_class(user)
        return Response(serializer.data)


class MovieListView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request):
        movies = Movie.objects.prefetch_related('cast').all()

        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data)


class MovieDetailView(RetrieveAPIView):
    queryset = Movie
    serializer_class = MovieSerializer


class ReservationView(CreateAPIView):
    serializer_class = ReservationSerializer
    queryset = Reservation
    permission_classes = [rest_framework.permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        movie = request.data['movie']
        id = Movie.objects.get(id=movie)
        serializer = MovieSerializer(id)
        return Response({'your desired movie':serializer.data})

    def post(self, request, pk):
        movie = Movie.objects.get(id=pk)
        if movie.tickets > 0:
            serializer = MovieSerializer(movie, data={'tickets': movie.tickets-1}, partial=True)
            reserv = self.queryset.objects.create(customer=request.user, movie=movie)
            if serializer.is_valid():
                serializer.save()
                reserv.save()
                return Response({'status':'success'}, status=200)
            else:
                return Response({'status':'error'})

        else:
            return Response({'status': 'no tickets'}, status=400)

