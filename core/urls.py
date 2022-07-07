from django.urls import path
from .views import Main, MovieListView


urlpatterns = [
    path('', Main.as_view()),
    path('movies/', MovieListView.as_view())
]