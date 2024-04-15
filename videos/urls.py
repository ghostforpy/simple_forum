from django.contrib import admin
from django.urls import path

from .views import MediaDetailView, MediaListView


urlpatterns = [
    path("", MediaListView.as_view(), name="media-index"),
    path("media/<int:pk>/", MediaDetailView.as_view(), name="media-detail"),
]
