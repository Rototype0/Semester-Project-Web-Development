from django.shortcuts import render, get_object_or_404
from games_list.models import Game
from django.core import serializers
from django.core.paginator import Paginator
import requests
import json
import time

def Home(request):
    number_of_games_per_page = 21
    url = 'https://api.steampowered.com/IStoreService/GetAppList/v1/?key=9CCFEAB8694DD2F007E55F87C3C523F6'
    '&include_games=true'
    '&include_dlc=false'
    '&include_software=false'
    '&include_videos=false'
    '&include_hardware=false'
    #'&last_appid=0'
    '&max_results=' + str(number_of_games_per_page)
    response = requests.get(url)
    data = response.json()

    paginator = Paginator(data['response']['apps'], number_of_games_per_page)
    page = request.GET.get('page')

    apps = paginator.get_page(page)
    

    for app in apps:
        url = 'https://store.steampowered.com/api/appdetails?appids=' + str(app["appid"])
        response = requests.get(url)
        data = response.json()
        app.update(data[str(app["appid"])]["data"])

    return render(request, 'home/game_list.html', {'games': apps})

def About(request):
    context = {
        'title': 'About',
    }
    return render(request, 'home/about.html', context)
