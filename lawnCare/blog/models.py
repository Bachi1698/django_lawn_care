from django.db import models

# Create your models here.
class Blog(models.Model):
    image = models.ImageField("images/Blog")
    description = models.TextField(max_length=255)
    titre = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "blog"
        verbose_name_plural = "blogs"

    def __str__(self):
        return self.titre

class Gallery(models.Model):
    titre = models.CharField(max_length=255)
    image = models.ImageField("images/Gallery")
    appreciation = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "gallery"
        verbose_name_plural = "gallerys"

    def __str__(self):
        return self.titre


