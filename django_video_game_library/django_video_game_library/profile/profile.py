from django.contrib.auth.models import User
from django.db import models
from django import forms
from .models import Profile
from django.shortcuts import render, redirect
from .forms import ProfileForm
from django.urls import path
from . import views

STATIC_URL = '/static/'

STATICFILES_DIRS = [BASE_DIR / "static"]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.CharField(
        max_length=255,
        choices=[
            ('pic1', 'Picture 1'),
            ('pic2', 'Picture 2'),
            ('pic3', 'Picture 3'),
            ('pic4', 'Picture 4'),
            ('pic5', 'Picture 5'),
            ('pic6', 'Picture 6'),
            ('pic7', 'Picture 7'),
            ('pic8', 'Picture 8'),
            ('pic9', 'Picture 9'),
            ('pic10', 'Picture 10'),
        ],
        default='pic1'
    )
    def __str__(self):
        return f"{self.user.username}'s Profile"

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']
        widgets = {
            'profile_picture': forms.RadioSelect
        }

def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Replace 'profile' with your profile page's URL name
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'profile.html', {'form': form, 'profile': profile})

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
]