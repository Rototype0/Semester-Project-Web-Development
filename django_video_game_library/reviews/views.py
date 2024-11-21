from django.shortcuts import render
from .models import Review, Rating
from django.shortcuts import render, get_object_or_404
from games_list.models import Game
#from .models import Review, Rating

def Demo(request):
    return render(request, 'reviews/demo.html')

def About(request):
    context = {
        'title': 'About',
    }
    return render(request, 'reviews/about.html', context)

def Home(request, appid):
    game = get_object_or_404(Game, appid=appid)
    reviews = Review.objects.filter(appid=appid)
    ratings = Rating.objects.filter(appid=appid)

    return render(request, 'Home.html', {
        'game': game,
        'reviews': reviews,
        'ratings': ratings,
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