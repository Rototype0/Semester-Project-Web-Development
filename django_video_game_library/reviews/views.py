from django.shortcuts import render
from .models import Review
# Create your views here.

reviews = [
    {
        'author': 'Hristo',
        'content': 'This game sucks >:(',
        'date_posted': '9/20/2024',
    },
    {
        'author': 'NotHristo',
        'content': 'I love this game :D',
        'date_posted': '9/20/2024',
    },
]

def Home(request):
    context = {
        'reviews': Review.objects.all(),
        'title': 'Reviews',
    }
    return render(request, 'reviews/home.html', context)

def About(request):
    context = {
        'title': 'About',
    }
    return render(request, 'reviews/about.html', context)