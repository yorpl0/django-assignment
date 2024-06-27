from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='movies/', blank=True)
    description = models.TextField()
    director = models.CharField(max_length=255, default='Unknown')  # Default value for director
    genre = models.CharField(max_length=100, default='Unknown')  # Default value for genre
    release_date = models.DateField(null=True, blank=True)  # Allow null or provide a valid default date

    def __str__(self):
        return self.title
