from django.db import models
from django.utils import timezone


class Cluster(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    importance = models.IntegerField()


    def __str__(self):
        return self.title