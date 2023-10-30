from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!',
                    'anotherboldmessage': 'you had it coming!'}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse("<a href='/rango/'>Index</a> Rango says here is the about page.")