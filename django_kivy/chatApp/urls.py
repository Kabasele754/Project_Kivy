from django.urls import path
from .views import *

urlpatterns = [
    path('', all_friend, name='all_friend'),
    path('create', create_friend, name='create_friend')
]