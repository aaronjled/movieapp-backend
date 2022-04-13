from django.urls import path
from . import views

urlpatterns = [
    path('api/movies', views.MovieList.as_view(), name='movie_list'), # api/contacts will be routed to the MovieList view for handling
    path('api/movies/<int:pk>', views.MovieDetail.as_view(), name='movie_detail'), # api/contacts will be routed to the MovieDetail view for handling
]