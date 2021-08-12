from django.urls import path
from .view import blogListView


urlpatterns=[
    path('', blogListView.as_view(), name='home'),
]