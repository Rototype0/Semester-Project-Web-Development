from django.shortcuts import render
import requests
import time

def Home(request):
    number_of_games_per_page = 21
    last_appid = request.GET.get('last_appid')

    base_url = ('https://api.steampowered.com/IStoreService/GetAppList/v1/?key=9CCFEAB8694DD2F007E55F87C3C523F6'
    '&include_games=true'
    '&include_dlc=false'
    '&include_software=false'
    '&include_videos=false'
    '&include_hardware=false'
    '&last_appid=' + str(last_appid) + ''
    '&max_results=' + str(number_of_games_per_page))

    response = requests.get(base_url)
    data = response.json()

    last_appid = data['response']['last_appid']
    apps = data['response']['apps']

    for app in apps:
        print("done with app: " + str(app["appid"]))
        url = 'https://store.steampowered.com/api/appdetails?appids=' + str(app["appid"]) + '&filters=basic'
        response = requests.get(url)
        data = response.json()
        app.update(data[str(app["appid"])]["data"])
        url = 'https://store.steampowered.com/appreviews/' + str(app["appid"]) + '?json=1'
        response = requests.get(url)
        data = response.json()
        app.update(data["query_summary"])
    return render(request, 'games_list/home.html', {'games': apps, 'last_appid': last_appid, 'example_url': base_url})

def About(request):
    context = {
        'title': 'About',
    }
    return render(request, 'games_list/about.html', context)
