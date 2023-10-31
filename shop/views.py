from django.shortcuts import render
from .models import *

# Create your views here.

def shop(request):
    artikels = Artikel.objects.all()
    content = {
        'artikels': artikels,
    }
    return render(request, 'shop/shop.html', content)

def warenkorb(request):
    if request.user.is_authenticated:
        kunde = request.user.kunde
        bestellung, created = Bestellung.objects.get_or_create(kunde=kunde, erledigt=False)
        artikels = bestellung.bestellteartikel_set.all()
    else:
        artikels = []
        bestellung = []
        
    content = {"artikels": artikels, "bestellung": bestellung}
    return render(request, 'shop/warenkorb.html', content)

def kasse(request):
    return render(request, 'shop/kasse.html')
