from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Kunde)
admin.site.register(Bestellung)
admin.site.register(Adresse)
admin.site.register(Artikel)
admin.site.register(BestellteArtikel)
