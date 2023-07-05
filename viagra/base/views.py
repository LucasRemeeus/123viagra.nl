from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

from .forms import medicijnForm, RegisterUserForm, CollectionForm
from .models import Medicine, Collection


# Create your views here.

@login_required
def index(request):
    context = {}
    return render(request, "base/index.html", context)


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
def afhaalactie(request):
    context = {}
    return render(request, "base/afhaalactie.html", context)


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


def medicijn_delete(request, pk):
    medicijn = Medicine.objects.get(pk=pk)
    medicijn.delete()
    return redirect("medicijnen")


@login_required
def afhaalactie(request):
    collectionlijst = Collection.objects.all()

    if request.method == "POST":
        form = CollectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("afhaalactie")
    else:
        form = CollectionForm()

    context = {'collections': collectionlijst, "form": form}
    return render(request, "base/afhaalactie.html", context)
