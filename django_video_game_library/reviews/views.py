from django.shortcuts import render
from .models import Review, Rating
def Demo(request):
    return render(request, 'reviews/demo.html')

def Home(request):
    reviews = Review.objects.all()
    for review in reviews:
        rating = Rating.objects.filter(review=review, user=request.user).first()
        review.user_rating = rating.rating if rating else 0
    return render(request, 'reviews/home.html', {"reviews": reviews})


def rate(request, post_id: int, rating: int):
    review = Review.objects.get(id=review_id)
    Rating.objects.filter(review=review, user=request.user).delete()
    review.rating_set.create(user=request.user, rating=rating)
    return index(request)


def About(request):
    context = {
        'title': 'About',
    }
    return render(request, 'reviews/about.html', context)

"""def index(request)
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