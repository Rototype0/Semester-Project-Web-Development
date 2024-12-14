from django.shortcuts import render
from .models import Review, Rating
from django.shortcuts import render, get_object_or_404, redirect
from games_list.models import Game
from django.http import HttpResponseRedirect
from django.urls import reverse
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

    return render(request, 'reviews/home.html', {
        'game': game,
        'reviews': reviews,
        'ratings': ratings,
    })

def like_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.user in review.likes.all():
        review.likes.remove(request.user)  # Unlike
    else:
        review.likes.add(request.user)  # Like
    return redirect(reverse('review-detail', args=[review_id]))

"""def Likes(request, appid):       #what is post_id in this case
    user = request.user
    rev = Review.objects.get(appid = appid)
    current_likes = rev.likes
    liked = Likes.objects.filter(user = request.user, rev = rev).count()
    if not liked:
        liked = Likes.objects.create(user = request.user, rev = rev)
        current_likes = current_likes+1
    else:
        liked = Likes.objects.filter(user = request.user, rev = rev).delete()
        current_likes = current_likes-1
    rev.likes = current_likes
    rev.save()
    return HttpResponseRedirect(reverse('reviews', args=[appid]))"""


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