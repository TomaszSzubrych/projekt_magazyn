import csv

from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv
from django.contrib import messages
from .models import *
from .forms import MagazynCreateForm, MagazynSearchForm, MagazynUpdateForm


def startowa(request):
    title = 'Witaj na stronie głównej'
    form = 'Witaj na stronie głównej'
    context = {
        "title": title,
        "test": form,
    }
    return render(request, "strona_startowa.html", context)


def lista_produktow(request):
    header = 'Lista Produktów'
    form = MagazynSearchForm(request.POST or None)
    queryset = Magazyn.objects.all()
    context = {
        "header": header,
        "queryset": queryset,
        "form": form,
    }
    if request.method == 'POST':
        queryset = Magazyn.objects.filter(#kategoria__icontains=form['kategoria'].value(),
                                          produkt__icontains=form['produkt'].value()
                                          )

        if form['export_do_CSV'].value():
            response = HttpResponse(content_type='txt/csv')
            response['Content-Disposition'] = 'attachment; filename="Lista Magazynu.csv"'
            writer = csv.writer(response)
            writer.writerow(['KATEGORIA', 'PRODUKT', 'ILOŚĆ'])
            instance = queryset
            for magazyn in instance:
                writer.writerow([magazyn.kategoria, magazyn.produkt, magazyn.ilosc])
            return response
        context = {
            "form": form,
            "header": header,
            "queryset": queryset,
        }
    return render(request, "lista_produktow.html", context)


def dodaj_produkt(request):
    form = MagazynCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Zapisane Pomyślnie')
        return redirect('/lista_produktow')
    context = {
        "form": form,
        "title": "Dodaj Produkt",
    }
    return render(request, "dodaj_produkt.html", context)


def aktualizuj_produkt(request, pk):
    queryset = Magazyn.objects.get(id=pk)
    form = MagazynUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = MagazynUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Zapisane Pomyślnie')
            return redirect('/lista_produktow')

    context = {
        'form': form
    }
    return render(request, 'dodaj_produkt.html', context)


def usun_produkt(request, pk):
    queryset = Magazyn.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Usunięto Pomyślnie')
        return redirect('/lista_produktow')
    return render(request, 'usun_produkt.html')
