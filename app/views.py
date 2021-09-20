from django.shortcuts import render, redirect
from .models import Card
from .forms import AddCard
from django.contrib import messages

# Create your views here.
def home(req):
    return render(req,'home.html',{})

def about(request):
    from app.tobecalled import generateArry
    return render(request, "about.html", {'list': generateArry()})

def addCard(req):
    return render(req,'addCard.html',{})

def card(req):
    all_cards = Card.objects.all
    return render(req,'card.html',{'all_cards':all_cards})

def reqYahoo(request):
    from app.tobecalled import reqYhaoo
    return render(request, "reqYhaoo.html", {'y': reqYhaoo()})
