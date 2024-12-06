from django.shortcuts import render
from games_list.models import Game
import requests
from django.core.paginator import Paginator
from concurrent.futures import ThreadPoolExecutor
from django.forms.models import model_to_dict

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

def Home(request):

    paginator = Paginator(Game.objects.all(), 21)
    page = request.GET.get('page')

    
    paginator_page = paginator.get_page(page)
    apps = paginator.page(page)

    apps_as_dict = list(apps.object_list.values())

    appids = []
    for app in apps:
        appids.append(app.appid)

    reviews = fetch_reviews_for_multiple_apps(appids)

    print(reviews)

    for app in apps_as_dict:
        print(app['name'])
        print(reviews[app['appid']]['query_summary'])
        app.update(reviews[app['appid']]['query_summary'])

    return render(request, 'games_list/home.html', {'games': apps_as_dict, 'paginator': paginator_page})

def About(request):
    context = {
        'title': 'About',
    }
    return render(request, 'games_list/about.html', context)
