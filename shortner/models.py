from django.db import models

class Urls(models.Model):
    link = models.CharField(max_length=50000)
    uid = models.CharField(max_length=10)
