from django.shortcuts import render
from .models import Spot

def index(request): 
    return render(request, 'index.html')

def spot_detail(request, pk):
    spot = Spot.objects.filter(slug=pk).first()
    context = {
        'spot': spot,
    }
    return render(request, 'spot-details.html', context)
