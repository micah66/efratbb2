from django.shortcuts import render
from .models import D1_Game


# Create your views here.
def index(request):
    return render(request, 'efratbb/index.html')

def schedule(request):
    games = D1_Game.objects.all()
    return render(request, 'efratbb/schedule.html', { 'games': games })

def standings(request):
    return render(request, 'efratbb/standings.html')

def register(request):
    return render(request, 'efratbb/register.html')

def comments(request):
    return render(request, 'efratbb/comments.html')

def gallery(request):
    return render(request, 'efratbb/gallery.html')

def contacts(request):
    return render(request, 'efratbb/contacts.html')
