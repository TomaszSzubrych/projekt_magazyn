from django import forms
from .models import Magazyn


class MagazynCreateForm(forms.ModelForm):
    class Meta:
        model = Magazyn
        fields = ['kategoria', 'produkt', 'ilosc']

    def clean_kategoria(self):
        kategoria = self.cleaned_data.get('kategoria')
        if not kategoria:
            raise forms.ValidationError('To pole jest wymagane')
        #
        # for instance in Magazyn.objects.all():
        #     if instance.kategoria == kategoria:
        #         raise forms.ValidationError(str(kategoria) + 'już istnieje')
        return kategoria

    def clean_produkt(self):
        produkt = self.cleaned_data.get('produkt')
        if not produkt:
            raise forms.ValidationError('To pole jest wymagane')

        return produkt


class MagazynSearchForm(forms.ModelForm):
    export_do_CSV = forms.BooleanField(required=False)
    class Meta:
        model = Magazyn
        fields = ['kategoria', 'produkt']


class MagazynUpdateForm(forms.ModelForm):
    class Meta:
        model = Magazyn
        fields = ['kategoria', 'produkt', 'ilosc']

