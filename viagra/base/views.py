from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import login
from django.contrib import messages

from .forms import medicijnForm, RegisterUserForm, CollectionForm
from .models import Medicine, Collection, Profile


# Create your views here.

@login_required
def index(request):
    profile = Profile.objects.get(user=request.user)

    context = {"profile": profile}
    return render(request, "base/index.html", context)


@login_required
def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        form = RegisterUserForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = RegisterUserForm(instance=profile)

    context = {"form": form, "profile": profile}
    return render(request, "base/profile_edit.html", context)


@login_required
def password_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = PasswordChangeForm(user=request.user, data=request.POST)

    context = {"form": form, "profile": profile}
    return render(request, "base/password_edit.html", context)


def register(request):
    if request.method == "POST":
        form1 = UserCreationForm(request.POST)
        form2 = RegisterUserForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user = form1.save()

            profilesave = form2.save(commit=False)
            profilesave.user = user
            profilesave.save()

            login(request, user)
            return redirect("index")
    else:
        form1 = UserCreationForm()
        form2 = RegisterUserForm()
    context = {"form1": form1, "form2": form2}
    return render(request, "registration/register.html", context)


@login_required
def medicijnen(request):
    medicijnenlijst = Medicine.objects.all()

    if request.method == "POST":
        form = medicijnForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("medicijnen")
    else:
        form = medicijnForm()

    context = {'medicijnen': medicijnenlijst, "form": form}
    return render(request, "base/medicijnen.html", context)


@login_required
def medicijnen_edit(request, pk):
    medicijnenedit = Medicine.objects.get(pk=pk)
    medicijnenlijst = Medicine.objects.all()

    if request.method == "POST":
        form = medicijnForm(request.POST, instance=medicijnenedit)
        if form.is_valid():
            form.save()
            return redirect("medicijnen")
    else:
        form = medicijnForm(instance=medicijnenedit)

    context = {'medicijnen': medicijnenlijst, "form": form}
    return render(request, "base/medicijnen.html", context)


@login_required
def medicijn_delete(request, pk):
    medicijn = Medicine.objects.get(pk=pk)
    medicijn.delete()
    return redirect("medicijnen")


@login_required
def afhaalactie(request):
    user = request.user

    if user.is_staff:
        collectionlijst = Collection.objects.filter(collectedApproved=False)
        collectionlijstapproved = Collection.objects.filter(collectedApproved=True)
    else:
        collectionlijst = Collection.objects.filter(user=user, collectedApproved=False)
        collectionlijstapproved = Collection.objects.filter(collectedApproved=True, user=request.user)

    if request.method == "POST":
        form = CollectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("afhaalactie")
    else:
        form = CollectionForm()

    context = {'collections': collectionlijst, 'collectionsapproved': collectionlijstapproved, "form": form}
    return render(request, "base/afhaalactie.html", context)


@login_required
def afhaalactie_delete(request, pk):
    collecting = Collection.objects.get(pk=pk)
    collecting.delete()
    return redirect("afhaalactie")


@login_required
def afhaalactie_afhalen(request, pk):
    collecting = Collection.objects.get(pk=pk)
    collecting.collected = True
    collecting.save()
    return redirect("afhaalactie")


@login_required
def afhaalactie_aproven(request, pk):
    collecting = Collection.objects.get(pk=pk)
    if collecting.collected:
        collecting.collectedApproved = True
        collecting.collectedApprovedBy = request.user
        collecting.save()
    return redirect("afhaalactie")
