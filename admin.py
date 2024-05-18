from django.contrib import admin
from .forms import MagazynCreateForm

from .models import *


class MagazynCreateAdmin(admin.ModelAdmin):
    list_display = ['kategoria', 'produkt', 'ilosc']
    form = MagazynCreateForm
    list_filter = ['kategoria']
    search_list = ['kategoria', 'produkt']


admin.site.register(Magazyn, MagazynCreateAdmin)
admin.site.register(Kategoria)