from django import forms
from corporation_site import models


class Create_event_form(forms.ModelForm):
    class Meta():
        model = models.Event
        fields = ['name', 'guests', 'budget', 'description', 'date']


class Assign_team_event_form(forms.Form):
    team = forms.ModelChoiceField(queryset=models.Team.objects.all(), label="Выберите команду")
    event = forms.ModelChoiceField(queryset=models.Event.objects.all(), label="Выберите мероприятие")