from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.all_friend, name='all_friend'),
    path('create', views.create_friend, name='create_friend')
]