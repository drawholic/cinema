from django.urls import path
from .views import  MovieListView, ReservationView, MovieDetailView, UserMoviesView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('movies/', MovieListView.as_view()),
    path('movies/<int:pk>/', MovieDetailView.as_view()),
    path('movies/<int:pk>/reserve/', ReservationView.as_view()),
    path('token/', obtain_auth_token),
    path('movies/reserved/', UserMoviesView.as_view())
]