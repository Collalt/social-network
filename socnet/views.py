from django.contrib.auth import login as auth_login
from django.shortcuts import render, reverse, redirect
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm


def dashboard(request):
    if request.method == "POST":
        data = request.POST
        action = data.get("start")
        if action == "login":
            return redirect(reverse("socnet:login"))
        elif action == "register":
            return redirect(reverse("socnet:register"))
    return render(request, "base.html")


def login(request):
    if request.method == "POST":
        data = request.POST
        # action = data.get("start")
        # if action == "login":
        #     return redirect(reverse("socnet:login"))
        # elif action == "register":
        #     return redirect(reverse("socnet:register"))
    return render(request, "base.html")


def register(request):
    if request.method == "GET":
        return render(
            request, "register.html",
        )
    elif request.method == "POST":
        form = UserCreationForm(request.POST)
        print(request.POST)
        for field in form:
            print("Field Error:", field.name, field.errors)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
        else:
            return render(
                request, "register.html")
        return redirect(reverse("socnet:profile_list"))

@login_required()
def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, 'socnet/profile_list.html', {'profiles': profiles})

@login_required()
def profile(request, pk):
    # if not hasattr(request.user, 'profile'):
    #     missing_profile = Profile(user=request.user)
    #     missing_profile.save()

    profile = Profile.objects.get(pk=pk)

    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("friend")
        if action == "edit":
            data = request.POST
            form = ProfileForm(request.POST, request.FILES)
            current_user_profile.bio = form['bio'].value()
            current_user_profile.avatar = form['avatar'].value()
        if action == "befriend":
            current_user_profile.friends.add(profile)
        elif action == "unfriend":
            current_user_profile.friends.remove(profile)
        current_user_profile.save()
    return render(request, 'socnet/profile.html', {'profile': profile})
# Create your views here.
