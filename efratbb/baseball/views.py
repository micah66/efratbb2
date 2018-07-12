from django.shortcuts import render
from .models import D1_Game, D2_Game, D3_Game


# Create your views here.
def index(request):
    return render(request, 'efratbb/index.html')

def schedule(request):
    d1_games = D1_Game.objects.all()
    d2_games = D2_Game.objects.all()
    d3_games = D3_Game.objects.all()
    context = {
        'd1_games': d1_games,
        'd2_games': d2_games,
        'd3_games': d3_games
    }
    return render(request, 'efratbb/schedule.html', context)

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
