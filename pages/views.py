from django.shortcuts import render
from django.utils.translation import ugettext as _  # pour test langue


def home(request):
    return render(request, "pages/home.html", {})


def codage(request):
    return render(request, "pages/codage.html", {})


def webdesign(request):
    return render(request, "pages/webdesign.html", {})


def intropython(request):
    return render(request, "pages/intropython.html", {})


def about(request):
    return render(request, "pages/about.html", {})


def contact(request):
    return render(request, "pages/contact.html", {})


def education(request):
    return render(request, "pages/education.html", {})


def translate(request):
    return render(request, "pages/translate.html", {})


def training(request):
    return render(request, "pages/training.html", {})


def workshop(request):
    return render(request, "pages/workshop.html", {})

