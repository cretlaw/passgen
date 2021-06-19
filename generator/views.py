import generator
from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, "generator/home.html")


def password(request):
    thepassword = "testing"
    characters = list("qwertyuiopasdfghjklzxcvbnm")
    length = int(request.GET.get("length"))

    if request.GET.get("uppercase"):
        characters.extend("QWERTYUIOPASDFGHJKLZXCVBNM")

    if request.GET.get("specials"):
        characters.extend("!@#$%^&*()")

    if request.GET.get("numbers"):
        characters.extend("123456789")

    thepassword = ""
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, "generator/password.html", {"password": thepassword})
