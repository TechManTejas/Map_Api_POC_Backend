from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(default="", max_length=255)
    lat_lon = models.JSONField(default=dict)

    def __str__(self):
        return self.name
