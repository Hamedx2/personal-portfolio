from django.db import models
class post(models.Model):
    title = models.CharField(max_length=200)
    discription = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(blank=True,upload_to='blog/')
    def __str__(self):
        return self.title
