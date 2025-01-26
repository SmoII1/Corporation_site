from django.http import HttpResponse
from django.shortcuts import render, redirect
from corporation_site import models
from corporation_site import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.utils.dateparse import parse_date



def main(request):
    a = render(request, 'main.html')
    return a


def employees(request):
    employees_spisok = models.Employee.objects.all()
    a = render(request, 'employees.html', context={'employees_spisok': employees_spisok})
    return a


def employee(request, employee_id):
    try:
        employee = models.Employee.objects.get(id=employee_id)
        a = render(request, 'employee.html', context={'employee': employee})
        return a
    except models.Employee.DoesNotExist:
        b = render(request, '404.html')
        return b


def create_event_form(request):
    if request.method == 'GET':
        form = forms.Create_event_form()
        a = render(request , 'create_event_form.html', context={'form': form})
        return a
    else:
        form = forms.Create_event_form(request.POST)
        if form.is_valid() == True:
            form.save()
            form = forms.Create_event_form()
        a = render(request , 'create_event_form.html', context={'form': form})
        return a


def event(request, event_id):
    try:
        event = models.Event.objects.get(id=event_id)
        a = render(request, 'event.html', context={'event': event})
        return a
    except models.Event.DoesNotExist:
        b = render(request, '404.html')
        return b


def events(request):
    get = request.GET.get('date')
    if get is None:
        events_spisok = models.Event.objects.all()
    else:
        events_spisok = models.Event.objects.filter(date=parse_date(get))
    a = render(request, 'events.html', context={'events_spisok': events_spisok})
    return a


def assign_team_event(request):
    if request.method == 'POST':
        form = forms.Assign_team_event_form(request.POST)
        if form.is_valid():
            team = form.cleaned_data['team']
            event = form.cleaned_data['event']
            team.event = event
            team.save()
            return redirect('home')
    else:
        form = forms.Assign_team_event_form()
    return render(request, 'assign_team_event_form.html', {'form': form})


def log_in(request):
    if request.method == "GET":
        a = render(request, 'login.html')
        return a
    else:
        user = request.POST['username']
        password = request.POST['user_password']
        a = authenticate(request, username=user, password=password)
        if a != None:
            login(request, a)
            b = redirect('main')
            return b
        else:
            b = render(request, 'login.html')
            return b


def log_out(request):
    logout(request)
    return redirect('main')
