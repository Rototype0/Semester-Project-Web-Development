import requests
import json
from django.shortcuts import render
from .models import Game, GameData
import time
from concurrent.futures import ThreadPoolExecutor


def Game_Info(request, appid):
    url = 'https://store.steampowered.com/api/appdetails?appids=' + appid
    response = requests.get(url)
    data = response.json()

    return render(request, 'games_list/game.html', {'game_info': data[appid]["data"]})

def import_data(request):
    if request.method == 'POST' and request.FILES['json_file']:

        for row in Game.objects.all().reverse():
            if Game.objects.filter(appid=row.appid).count() > 1:
                print('Deleting: ' + row.name)
                row.delete()

        
        json_file = request.FILES['json_file']
        data = json.load(json_file)
        for item in data['response']['apps']:
            if Game.objects.filter(appid=item['appid']).exists():
                print(str(item['name']) +' already Exists')
                if not GameData.objects.filter(appid=Game.objects.filter(appid=item['appid'])[0]).exists():
                    print(str(item['name']) +' does not have a GameData object!')
            else:
                game = Game(
                    appid=item['appid'],
                    name=item['name'],
                )
                url = 'https://store.steampowered.com/api/appdetails?appids=' + str(item['appid']) + '&filters=basic'
                response = requests.get(url)
                json_game_data = response.json()
                
                time.sleep(0.75)

                if json_game_data != None:
                    if json_game_data[str(item['appid'])]['success'] == True:
                        game.save()
                        print(str(item['appid']))
                        json_game_data = json_game_data[str(item['appid'])]['data']
                        game_data = GameData(
                            appid = game,
                            is_free = json_game_data['is_free'],
                            supported_languages = json_game_data['supported_languages'],
                            detailed_description = json_game_data['detailed_description'],
                            short_description = json_game_data['short_description'],
                            header_image = json_game_data['header_image']
                        )
                        game_data.save()
                else:
                    print("got rate limited")
                    time.sleep(60)
        return render(request, 'success.html')
    return render(request, 'form.html')


def About(request):
    return render(request, 'games_list/about.html')