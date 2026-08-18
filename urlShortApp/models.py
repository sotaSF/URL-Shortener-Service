from django.db import models

# Create your models here.

class ShortUrl(models.Model):
    shortUrl = models.CharField(max_length=10,unique=True)
    mainUrl = models.CharField(max_length=2048)
    accessed = models.IntegerField(default=0)

