from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'efratbb/index.html')

def schedule(request):
    return render(request, 'efratbb/schedule.html')

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
