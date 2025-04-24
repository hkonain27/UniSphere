from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Q
from .models import Profile, Group, Event, HousingListing, Message
from .forms import UserRegistrationForm, EventForm, HousingSearchForm, MessageForm


def landing_page(request):
    return render(request, 'base/landing_page.html')

def login_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'base/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

def register_user(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Registration failed')
    return render(request, 'base/sign_up.html', {'form': form})

@login_required
def dashboard(request):
    profile = Profile.objects.get(user=request.user)
    events = Event.objects.filter(attendees=profile)
    groups = profile.group_set.all()
    return render(request, 'base/home.html', {'profile': profile, 'events': events, 'groups': groups})

@login_required
def create_event(request):
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.host = request.user.profile
            event.save()
            return redirect('dashboard')
    return render(request, 'base/create_event.html', {'form': form})

def events_list(request):
    events = Event.objects.all()
    return render(request, 'base/events_list.html', {'events': events})

def about_us(request):
    return render(request, 'base/about_us.html')  # Make sure you have this template too
from django.shortcuts import render

# base/views.py
#from django.shortcuts import render
from .models import Job 


def job_search(request):
    jobs = Job.objects.all()
    return render(request, 'base/job_search.html', {'jobs': jobs})


def contact_us(request):
    return render(request, 'base/contact_us.html')  # Make sure this HTML file exists
from django.shortcuts import render

def layout(request):
    return render(request, 'base/layout.html')  # make sure this template exists

def group_discovery(request):
    groups = Group.objects.all()
    query = request.GET.get('q')
    if query:
        groups = groups.filter(country__icontains=query)
    return render(request, 'base/groups.html', {'groups': groups})

def job_api(request):
    jobs = Job.objects.all().values('jobtitle', 'compname', 'location', 'compdesc', 'complocation')
    return JsonResponse(list(jobs), safe=False)

@login_required
def join_group(request, group_id):
    group = Group.objects.get(id=group_id)
    group.members.add(request.user.profile)
    return redirect('group-discovery')

def housing_search(request):
    listings = HousingListing.objects.all()
    form = HousingSearchForm(request.GET or None)
    if form.is_valid():
        listings = listings.filter(
            location__icontains=form.cleaned_data['location']
        )
    return render(request, 'base/housing.html', {'form': form, 'listings': listings})

@login_required
def group_chat(request, group_id):
    group = Group.objects.get(id=group_id)
    messages_list = Message.objects.filter(group=group)
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.group = group
            message.sender = request.user.profile
            message.save()
            return redirect('group-chat', group_id=group.id)
    return render(request, 'base/chat.html', {'group': group, 'messages': messages_list, 'form': form})
