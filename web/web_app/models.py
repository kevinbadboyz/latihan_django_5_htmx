from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    author = models.CharField(max_length = 100)
    year = models.IntegerField(default = 2000)

    def __str__(self):
        return self.title
