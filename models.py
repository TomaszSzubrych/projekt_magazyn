from django.db import models

wybor_kategorii = (
    ('Sprzęt Komputerowy ', 'Sprzęt Komputerowy'),
    ('Meble Biurowe', 'Meble Biurowe'),
    ('Telefon', 'Telefon'),
    ('Podzespoły', 'Podzespoły'),
)


class Kategoria(models.Model):
    nazwa = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nazwa


class Magazyn(models.Model):
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE, blank=True)
    produkt = models.CharField(max_length=50, blank=True, null=True)
    ilosc = models.IntegerField(default='0', blank=True, null=True)
    przyjeta_ilosc = models.IntegerField(default='0', blank=True, null=True)
    przyjete_przez = models.CharField(max_length=50, blank=True, null=True)
    przekazana_ilosc = models.IntegerField(default='0', blank=True, null=True)
    przekazane_przez = models.CharField(max_length=50, blank=True, null=True)
    przekazane_do = models.CharField(max_length=50, blank=True, null=True)
    numer_telefonu = models.CharField(max_length=50, blank=True, null=True)
    utworzone_przez = models.CharField(max_length=50, blank=True, null=True)
    ponownie_zamowic = models.IntegerField(default='0', blank=True, null=True)
    ostatnia_aktualizacja = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.produkt
