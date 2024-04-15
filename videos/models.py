from django.db import models
from django.urls import reverse

# Create your models here.


class Media(models.Model):
    title = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        "users.User", on_delete=models.SET_NULL, null=True, blank=True
    )
    file = models.FileField(upload_to="media/")
    pic = models.ImageField(upload_to="pics", null=True, blank=True)

    def get_absolute_url(self):
        return reverse("media-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
