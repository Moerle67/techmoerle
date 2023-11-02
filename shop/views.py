from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
 
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
    if request.user.is_authenticated:
        kunde = request.user.kunde
        bestellung, created = Bestellung.objects.get_or_create(kunde=kunde, erledigt=False)
        artikels = bestellung.bestellteartikel_set.all()
    else:
        artikels = []
        bestellung = []
    content = {"artikels": artikels, "bestellung": bestellung}

    return render(request, 'shop/kasse.html', content)

def artikelBackend(request):
    daten = json.loads(request.body)
    artikelID = daten['artikelID']
    action = daten['action']
    kunde = request.user.kunde
    artikel = Artikel.objects.get(id=artikelID)
    bestellung, created = Bestellung.objects.get_or_create(kunde=kunde, erledigt=False)
    bestellteArtikel, created = BestellteArtikel.objects.get_or_create(bestellung=bestellung, artikel=artikel)

    if action == 'bestellen':
        bestellteArtikel.menge += 1
    elif action == 'entfernen':
        bestellteArtikel.menge -= 1

    bestellteArtikel.save()

    if bestellteArtikel.menge <= 0:
        bestellteArtikel.delete()
        
    return JsonResponse("Artikel hinzugefügt", safe = False)


