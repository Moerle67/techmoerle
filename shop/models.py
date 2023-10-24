from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Kunde(models.Model):
    benutzer = models.OneToOneField(User, verbose_name="Benutzer", on_delete=models.RESTRICT, null=True, blank=True)
    name = models.CharField("Name", max_length=200, null=True)
    email = models.CharField("E-Mail", max_length=200, null=True)
    

    class Meta:
        verbose_name = ("Kunde")
        verbose_name_plural = ("Kunden")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Kunde_detail", kwargs={"pk": self.pk})
    
class Artikel(models.Model):
    name = models.CharField("Name", max_length=200, null=True)
    beschreibung = models.TextField("Beschreibung", null=True, blank=True)
    preis = models.FloatField("Preis")
    bild = models.ImageField("Bild", blank=True, null=True)
    
    class Meta:
        verbose_name = ("Artikel")
        verbose_name_plural = ("Artikel")

    def __str__(self):
        return f"{self.name}/{self.preis}"

    def get_absolute_url(self):
        return reverse("Artikel_detail", kwargs={"pk": self.pk})

class Bestellung(models.Model):
    kunde = models.ForeignKey(Kunde, verbose_name=("Kunde"), on_delete=models.SET_NULL, null=True, blank=True)
    bestelldatum = models.DateTimeField("Bestelldatum", auto_now_add=True)
    erledigt = models.BooleanField("Erledigt", default=False, blank=True, null=True)
    auftrags_id = models.CharField("Auftrags ID", max_length=200, null=True)

    class Meta:
        verbose_name = "Bestellung"
        verbose_name_plural = "Bestellungen"

    def __str__(self):
        return f"({self.id} - {self.kunde}/{self.bestelldatum})"

    def get_absolute_url(self):
        return reverse("Bestellung_detail", kwargs={"pk": self.pk})
    

class BestellteArtikel(models.Model):
    artikel = models.ForeignKey(Artikel, verbose_name="Artikel", on_delete=models.SET_NULL, blank=True, null=True)
    bestellung = models.ForeignKey(Bestellung, verbose_name="Bestellung", on_delete=models.SET_NULL, blank=True, null=True)
    menge = models.IntegerField("Menge", default=0, null=True, blank=True)
    datum = models.DateTimeField("Datum", auto_now_add=True)

    class Meta: 
        verbose_name = "BestellteArtikel"
        verbose_name_plural = "BestellteArtikel"

    def __str__(self):
        return self.artikel.name

    def get_absolute_url(self):
        return reverse("BestellteArtikel_detail", kwargs={"pk": self.pk})

class Adresse(models.Model):
    kunde = models.ForeignKey(Kunde, verbose_name=("Kunde"), on_delete=models.SET_NULL, null=True, blank=True)
    bestellung = models.ForeignKey(Bestellung, verbose_name=("Bestellung"), on_delete=models.SET_NULL, null=True, blank=True)
    adresse = models.CharField(("Adresse"), max_length=200, null=True, blank=True)
    plz = models.CharField(("PLZ"), max_length=200, null=True, blank=True)
    stadt = models.CharField(("Stadt"), max_length=200, null=True, blank=True)
    land = models.CharField(("Bundesland"), max_length=200, null=True, blank=True)
    datum = models.DateTimeField("Adresse", auto_now_add=True)

    class Meta:
        verbose_name = "Adresse"
        verbose_name_plural = "Adressen"

    def __str__(self):
        return f"{self.kunde.name} ({self.datum})"

    def get_absolute_url(self):
        return reverse("Adresse_detail", kwargs={"pk": self.pk})
