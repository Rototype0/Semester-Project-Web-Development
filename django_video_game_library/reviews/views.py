from .models import Review, Rating
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now
from games_list.models import Game, Avg
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required

def Reviews(request, appid):
    game = get_object_or_404(Game, appid=appid)
    reviews = Review.objects.filter(appid=appid).order_by('-date_posted')
    ratings = Rating.objects.filter(appid=appid)
    avg_rating = ratings.aggregate(average=Avg('score'))['average']
    if request.method == 'POST' and 'review_submit' in request.POST:
        content = request.POST.get('content', '').strip()
        header = request.POST.get('header', 'Header').strip()

        if content:
            Review.objects.create(
                appid=appid,
                header=header,
                content=content,
                author=request.user,
                date_posted=now()
            )
            return redirect('game_lib_game', appid=appid)

    return render(request, 'game_list/game.html', {
        'game': game,
        'reviews': reviews,
        'ratings': ratings,
        'avg_rating': avg_rating,
    })

"""def Home(request):
    reviews = Review.objects.all()
    for review in reviews:
        rating = Rating.objects.filter(review=review, user=request.user).first()
        review.user_rating = rating.rating if rating else 0
    return render(request, 'reviews/home.html', {"reviews": reviews})


def rate(request, review_id: int, rating: int):
    review = Review.objects.get(id=review_id)
    Rating.objects.filter(review=review, user=request.user).delete()
    review.rating_set.create(user=request.user, rating=rating)
    return index(request, 'reviews/home.html', {"rating": rating})



    

def index(request)
    reviews = Review.objects.all
    for post in posts:
        rating = Rating.objects.filter(post=post, user=request.user).first()
        post.user_rating = rating.rating if rating else 0
    return render(request, "index.html", {"posts": posts})
"""
'''context = {
        'reviews': Review.objects.all(),
        'title': 'Reviews',
    }
    return render(request, 'reviews/home.html', context)'''