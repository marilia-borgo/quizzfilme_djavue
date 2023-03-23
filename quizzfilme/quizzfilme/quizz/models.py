from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg

class Personalidade(models.Model):
    resultado = models.CharField(max_length=512)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def to_dict_json(self):
        return {
            'id': self.id,
            'resultado': self.resultado,
        }

class Movie(models.Model):
    header = models.CharField(max_length=100, default="Header")
    text = models.TextField()

    def average_rating(self) -> float:
        return Rating.objects.filter(movie=self).aggregate(Avg("rating"))["rating__avg"] or 0

    def __str__(self):
        return f"{self.header}: {self.average_rating()}"


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.movie.header}: {self.rating}"
