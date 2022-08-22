
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home, name="home"),
    path('all',views.every_task,name="all"),
    path('add_task',views.add_task,name='add_task'),
    path('is_completed/<int:pk>',views.completed,name='is_completed'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('search',views.search, name='search')
]
