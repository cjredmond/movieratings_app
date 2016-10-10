from django.db import models
from django.db.models import Avg
from statistics import mean
from django.db.models import Count
import operator
# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length = 50)
    release_date = models.CharField(max_length = 50)
    video_release = models.CharField(max_length = 40)
    url = models.CharField(max_length = 150)
    unknown = models.CharField(max_length = 50)
    action_genre = models.BooleanField()
    adventure = models.BooleanField()
    animation = models.BooleanField()
    children = models.BooleanField()
    comedy = models.BooleanField()
    crime = models.BooleanField()
    documentary = models.BooleanField()
    drama = models.BooleanField()
    fantasy = models.BooleanField()
    film_noir = models.BooleanField()
    horror = models.BooleanField()
    musical = models.BooleanField()
    mystery = models.BooleanField()
    romance = models.BooleanField()
    sci_fi = models.BooleanField()
    thriller = models.BooleanField()
    war = models.BooleanField()
    western = models.BooleanField()
    average_rating = models.FloatField()

    def __str__(self):
        return self.title
    @property
    def avg_rating(self):
        return Rating.objects.filter(movie = self).aggregate(Avg('rating')).get('rating__avg')

    def update_avg(self):
        self.average_rating = self.avg_rating()
    @property
    def reviews(self):
        count = 0
        amount = Rating.objects.filter(movie=self)
        for x in amount:
            count = count +1
        return count

class Rater(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length = 1)
    occupation = models.CharField(max_length = 50)
    zip_code = models.CharField(max_length = 40)

    def __str__(self):
        return self.occupation
    @property
    def avg_rating(self):
        return Rating.objects.filter(rater = self).aggregate(Avg('rating')).get('rating__avg')



class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating = models.IntegerField()
    time_stamp = models.IntegerField()
