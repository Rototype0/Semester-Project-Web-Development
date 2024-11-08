import requests
import json
import time
from django.core import serializers
from django.shortcuts import render
from django.core.paginator import Paginator

def List(request):
    url = 'https://api.steampowered.com/ISteamApps/GetAppList/v0002/?key=STEAMKEY&format=json'
    response = requests.get(url)
    data = response.json()

    paginator = Paginator(data['applist']['apps'], 10)
    page = request.GET.get('page')

    apps = paginator.get_page(page)
    

    for app in apps:
        url = 'https://store.steampowered.com/api/appdetails?appids=' + str(app["appid"])
        response = requests.get(url)
        data = response.json()
        time.sleep(1)
        app.update(data[str(app["appid"])]["data"])

    return render(request, 'games_list/home.html', {'games': apps})

def Game_Info(request, appid):
    url = 'https://store.steampowered.com/api/appdetails?appids=' + appid
    response = requests.get(url)
    data = response.json()

    return render(request, 'games_list/game.html', {'game_info': data[appid]["data"]})
    

def About(request):
    return render(request, 'games_list/about.html')