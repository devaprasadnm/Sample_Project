from django.urls import path
from .views import *

urlpatterns = [
    path('articles',article_list),
    path('articles/<int:pk>/',article_details),
]