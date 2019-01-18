from django.db import models

# Create your models here.
class UrlLink(models.Model):
    website=models.URLField()

    def __str__(self):
        return self.website
    