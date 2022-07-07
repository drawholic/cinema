from django.urls import path
from .views import Main, MovieListView, BookingView


urlpatterns = [
    path('', Main.as_view()),
    path('movies/', MovieListView.as_view()),
    path('movies/<int:pk>/', BookingView.as_view())
]