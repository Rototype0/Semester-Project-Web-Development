from django.shortcuts import render
from games_list.models import Game
from games_list.models import GameData
from django.core.paginator import Paginator
import json, time, math, requests
from concurrent.futures import ThreadPoolExecutor


def Game_Info(request, appid):
    game = Game.objects.filter(appid=appid).first()
    reviews = fetch_app_reviews(appid)
    reviews_summary = reviews[1]['query_summary']

    total_reviews = reviews[1]['query_summary']['total_reviews']
    if total_reviews != 0:
        total_positive_reviews = reviews[1]['query_summary']['total_positive']
        reviews_score = total_positive_reviews / total_reviews
        reviews[1]['query_summary'].update({'review_score': round(reviews_score * 10, 1)})

    price_query = fetch_app_price(appid)
    price_overview = {}
    if price_overview != None:
        if price_query[1].get(str(appid),{}).get('success', False):
            if price_query[1].get(str(appid),{}).get('data', []) != []:
                price_overview = price_query[1].get(str(appid),{}).get('data', {}).get('price_overview', {})
                price_overview['initial'] = price_overview.get('initial') / 100
                price_overview['final'] = price_overview.get('final') / 100

    return render(request, 'games_list/game.html', {'game': game, 'reviews': reviews_summary, 'price_overview': price_overview})

def fetch_app_price(appid):
    url = f"https://store.steampowered.com/api/appdetails?filters=price_overview&appids={appid}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for HTTP errors
        return appid, response.json()
    except requests.exceptions.RequestException as e:
        return appid, {"error": str(e)}

def fetch_app_reviews(appid):
    """Fetch reviews for a specific appid."""
    url = f"https://store.steampowered.com/appreviews/{appid}?json=1&language=all&num_per_page=0&purchase_type=all"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for HTTP errors
        return appid, response.json()
    except requests.exceptions.RequestException as e:
        return appid, {"error": str(e)}

def fetch_reviews_for_multiple_apps(appids):
    results = {}
    with ThreadPoolExecutor() as executor:
        future_to_appid = {executor.submit(fetch_app_reviews, appid): appid for appid in appids}
        for future in future_to_appid:
            appid, data = future.result()
            results[appid] = data
    return results

def Games_List(request):

    paginator = None
    if request.method == "POST":
        searched = request.POST['searched']
        #apps_as_dict = list(Game.objects.filter(name__icontains=searched).values())
        paginator = Paginator(Game.objects.filter(name__icontains=searched), 21)
        #print(apps_as_dict)
    else: 
        paginator = Paginator(Game.objects.all(), 21)
    
    page = request.GET.get('page')

    if page == None:
        page = 1
    
    paginator_page = paginator.get_page(page)
    apps = paginator.get_page(page)

    apps_as_dict = list(apps.object_list.values())

    if request.method == "POST":
        searched = request.POST['searched']
        apps_as_dict = list(Game.objects.filter(name__icontains=searched).values())
        paginator_page = Game.objects.filter(name__icontains=searched)
        print(apps_as_dict)

    appids = []
    for app in apps_as_dict:
        appids.append(app['appid'])

    reviews = fetch_reviews_for_multiple_apps(appids)

    for app in apps_as_dict:
        #print(app['name'])
        #print(reviews[app['appid']]['query_summary'])
        total_reviews = reviews[app['appid']]['query_summary']['total_reviews']
        if total_reviews != 0:
            total_positive_reviews = reviews[app['appid']]['query_summary']['total_positive']
            reviews_score = total_positive_reviews / total_reviews
            reviews[app['appid']]['query_summary'].update({'review_score': round(reviews_score * 10, 1)})
        else:
            print(app['name'] + ' has zero reviews')

        app.update(reviews[app['appid']]['query_summary'])

    return render(request, 'games_list/home.html', {'games': apps_as_dict, 'paginator': paginator_page})

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
                    print(str(item['name']) +' does not have a GameData object!!!!!!!!')
                    url = 'https://store.steampowered.com/api/appdetails?appids=' + str(item['appid']) + '&filters=basic'
                    response = requests.get(url)
                    json_game_data = response.json()
                    
                    time.sleep(0.75)

                    if json_game_data != None:
                        if json_game_data[str(item['appid'])]['success'] == True:
                            print(str(item['appid']))
                            json_game_data = json_game_data[str(item['appid'])]['data']
                            game_data = GameData(
                                appid = game,
                                is_free = json_game_data.get('is_free', False),
                                supported_languages = json_game_data.get('supported_languages', 'English'),
                                detailed_description = json_game_data.get('detailed_description', 'Description'),
                                short_description = json_game_data.get('short_description', 'Description'),
                                header_image = json_game_data.get('header_image', 'Header image')
                            )
                            game_data.save()
                        else:
                            print("Could not build Gamedata object :(")
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
                            is_free = json_game_data.get('is_free', False),
                            supported_languages = json_game_data.get('supported_languages', 'English'),
                            detailed_description = json_game_data.get('detailed_description', 'Description'),
                            short_description = json_game_data.get('short_description', 'Description'),
                            header_image = json_game_data.get('header_image', 'Header image')
                        )
                        game_data.save()
                else:
                    print("got rate limited")
                    time.sleep(60)
        return render(request, 'success.html')
    return render(request, 'form.html')