from django.shortcuts import render
from games_list.models import Game
import requests
from django.core.paginator import Paginator
from concurrent.futures import ThreadPoolExecutor



def About(request):
    context = {
        'title': 'About',
    }
    return render(request, 'games_list/about.html', context)
