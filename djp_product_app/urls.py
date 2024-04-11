
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'movie_app'
urlpatterns = [
    path('',views.home,name='home'),
    path('movie/<int:movie_id>',views.movie_detail,name='details'),
    path('movie/add', views.movie_add, name='movie_add'),
    path('movie/update/<int:movie_id>', views.movie_update, name='movie_update'),
    path('movie/delete/<int:movie_id>',views.movie_delete,name='movie_delete')

]
