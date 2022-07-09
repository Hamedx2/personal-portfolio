from django.db import models

class project(models.Model):
    title = models.CharField(max_length=200)
    discription = models.TextField()
    date = models.DateTimeField(blank=True)
    image = models.ImageField(blank=True)
    link = models.URLField(blank=True)
    def __str__(self):
        return self.title
