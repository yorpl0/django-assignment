# movies/urls.py
from django.urls import path
from movies import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),  # URL for movie list
    path('movie/<int:movie_id>/', views.movie_detail_view, name='movie_detail'),  # URL for movie detail
    path('add/', views.add_movie, name='add_movie')
]
