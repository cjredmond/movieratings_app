from django.shortcuts import render
from movieratings.models import Movie,Rater,Rating
from django.http import HttpResponse
import operator
# Create your views here.
def get_av_for_movies():
    thing = {
    Movie.objects.first().title : Movie.objects.first().avg_rating
    }
    return thing

def attempt():
    mvs = Movie.objects.all()
    top = sorted(mvs, key=operator.attrgetter('avg_rating'))
    empty = []
    for x in top:
        empty.append(x)
    empty.reverse()

    return empty[:20]

def top_20_view(request):
    context = {
    'this' : get_av_for_movies(),
    'twenty' : attempt(),
    'top' : attempt()
    }
    return render(request, "top_20.html",context)

def index_view(request):
    context = {
    "all_movies" : Movie.objects.all()
    }
    return render(request, "index.html")

def all_movies_view(request):
    context = {
    "all_movies" : Movie.objects.all()
    }
    return render(request, "all_movies.html", context)

def all_raters_view(request):
    context = {
    "all_raters" : Rater.objects.all()
    }
    return render(request, "all_raters.html", context)

def movie_info_view(request, movie_id):
    context = {
    'movie' : Movie.objects.get(id=movie_id),
    'rating' : Rating.objects.filter(movie = movie_id)
    }
    return render(request, "movie_info.html", context)

def rater_info_view(request, rater_id):
    context = {
    'rater' : Rater.objects.get(id=rater_id),
    'movies' : Rating.objects.filter(rater = rater_id)
    }
    return render(request, "rater_info.html", context)
