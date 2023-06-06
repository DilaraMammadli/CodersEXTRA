from django.db import models
from .validator import validate_timestamp


class Book(models.Model):
    name = models.CharField(max_length = 100)
    author_name = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateField(blank=True, null=True, validator=[validate_timestamp])

    def __str__(self):
        return self.name
