from django.shortcuts import render, get_object_or_404
from games_list.models import Game
from django.core import serializers
from django.core.paginator import Paginator
import requests
import json
import time

def Home(request):
    url = 'https://api.steampowered.com/ISteamApps/GetAppList/v0002/?key=STEAMKEY&format=json'
    response = requests.get(url)
    data = response.json()

    paginator = Paginator(data['applist']['apps'], 20)
    page = request.GET.get('page')

    apps = paginator.get_page(page)
    

    for app in apps:
        url = 'https://store.steampowered.com/api/appdetails?appids=' + str(app["appid"])
        response = requests.get(url)
        data = response.json()
        time.sleep(2)
        app.update(data[str(app["appid"])]["data"])

    return render(request, 'home.html', {'games': apps})

def About(request):
    context = {
        'title': 'About',
    }
    return render(request, 'about.html', context)
