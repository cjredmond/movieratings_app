from django.shortcuts import render
from movieratings.models import Movie,Rater,Rating
from django.http import HttpResponse
# Create your views here.
def get_av_for_movies():
    thing = {
    Movie.objects.first().title : Movie.objects.first().avg_rating
    }
    return thing

def top_20_view(request):
    context = {
    'this' : get_av_for_movies()
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
    'title' : Movie.objects.get(id=movie_id)
    }
    return render(request, "movie_info.html", context)
