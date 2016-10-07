from django.contrib import admin
from movieratings.models import Rater, Movie, Rating
# Register your models here.
admin.site.register([Rater, Movie, Rating])
