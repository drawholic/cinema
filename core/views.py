from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer


class Main(GenericAPIView):
    def get(self, request):
        return Response({'status':'success'})


class MovieListView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request):
        movies = Movie.objects.all()

        for movie in movies:
            movie.cast.set(movie.cast.all())

        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


class BookingView(RetrieveUpdateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    def put(self, request, *args, **kwargs):
        return Response('okay, heres your ticket')

