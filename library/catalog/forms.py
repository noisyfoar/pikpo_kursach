from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Client
import datetime


class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Введите дату от настоящего момента до 4 недель (по умолчанию 3).")
    client = forms.ModelMultipleChoiceField(Client.objects.all())

    def clean_renewal_date(self):
        data = self.cleaned_data['return_date']
        client = self.cleaned_data['client']
        if data < datetime.date.today():
            raise ValidationError(_('Недействительная дата - продление в прошлом'))

        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Недействительная дата - продление более чем на 4 недели вперед'))

        return data, client
