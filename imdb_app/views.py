import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from datetime import date

# Create your views here.
def home(request):
    movie_data = get_imdb_movies()
    context = {'movie_data': movie_data}
    return render(request, "index.html", context)

def get_imdb_movies():
    current_date = date.today()
    current_year = current_date.strftime("%Y")
    next_year = str(int(current_year) + 1)
    url = "https://api.imdbapi.dev/titles?types=MOVIE&startYear="+ current_year + "&endYear=" + next_year + "&sortBy=SORT_BY_POPULARITY"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.text)
    data = response.json()
    new_data = data["titles"]
    return new_data

def tv_shows(request):
    tv_data = get_imdb_tvshows()
    context = {'tv_data': tv_data}
    return render(request, "tv-shows.html", context)

def get_imdb_tvshows():
    current_date = date.today()
    current_year = current_date.strftime("%Y")
    # next_year = str(int(current_year) + 1)
    url = "https://api.imdbapi.dev/titles?types=TV_SERIES&countryCodes=US&countryCodes=GB&sortBy=SORT_BY_POPULARITY&endYear="+ current_year
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    # print(response.text)
    data = response.json()
    new_data = data["titles"]
    return new_data

def about(request):

    return render(request, "about.html")