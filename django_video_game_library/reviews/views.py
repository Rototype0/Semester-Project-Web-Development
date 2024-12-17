from .models import OReview, Rating
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now
from games_list.models import Game
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

def OReviews(request, appid):
    game = get_object_or_404(Game, appid=appid)
    oreviews = OReview.objects.filter(appid=appid).order_by('-date_posted')
    ratings = Rating.objects.filter(appid=appid)
    avg_rating = ratings.aggregate(average=Avg('score'))['average']

    user_rating = None
    if request.user.is_authenticated:
        user_rating = Rating.objects.filter(appid=appid, user=request.user).first()

    if request.method == 'POST':
        if 'oreview_submit' in request.POST:
            content = request.POST.get('content', '').strip()
            header = request.POST.get('header', 'Header').strip()

            if content:
                OReview.objects.create(
                    appid=appid,
                    header=header,
                    content=content,
                    author=request.user,
                    date_posted=now()
                )
                return redirect('game_lib_game', appid=appid)

        elif 'rating_submit' in request.POST:
            score = request.POST.get('rating')
            if score:
                score = int(score)
                if 1 <= score <= 10:
                    rating, created = Rating.objects.get_or_create(
                        appid=appid,
                        user=request.user,
                        defaults={'score': score}
                    )
                    if not created:
                        rating.score = score
                        rating.save()
                return redirect('game_lib_game', appid=appid)

    return render(request, 'reviews/home.html', {
        'game': game,
        'oreviews': oreviews,
        'user_rating': user_rating,
        'ratings': ratings,
        'avg_rating': avg_rating,
    })