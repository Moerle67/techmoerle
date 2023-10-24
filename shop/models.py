from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Kunde(models.Model):
    benutzer = models.OneToOneField(User, verbose_name="Benutzer", on_delete=models.RESTRICT, null=True, blank=True)
    name = models.CharField("Name", max_length=200, null=True)
    email = models.CharField("E-Mail", max_length=200, null=True)
    

    class Meta:
        verbose_name = _("Kunde")
        verbose_name_plural = _("Kunden")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Kunde_detail", kwargs={"pk": self.pk})
