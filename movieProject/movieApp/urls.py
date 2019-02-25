from django.urls import path

from . import views

urlpatterns = [
    path('movies/', views.index, name='base'),
    path('movie_details/', views.movie_details, name='movie_details'),
    path('movie_synopsis/', views.movie_synopsis, name='movie_synopsis'),

]