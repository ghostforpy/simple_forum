# from django.shortcuts import render, reverse
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.views.generic.edit import FormMixin
from django.views.generic import (
    ListView,
    DetailView,
)

# from django.views.generic.list import BaseListView

from .models import Media

# Topic views


class MediaListView(ListView):
    model = Media
    # template_name = "videos/index.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "medias"
    # paginate_by = 5


class MediaDetailView(DetailView):
    model = Media
