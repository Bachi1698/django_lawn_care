from django.db import models

# Create your models here.
class Service(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField("images/Service")
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "service"
        verbose_name_plural = "services"

    def __str__(self):
        return self.nom

class Conseil(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField("images/Conseil")
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "conseil"
        verbose_name_plural = "conseils"

    def __str__(self):
        return self.nom

