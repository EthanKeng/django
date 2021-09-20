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
    if req.method=='POST':
        form=AddCard(req.POST or None)
        if form.is_valid():
            form.save()
            messages.success(req,('Card has been added'))
            return redirect('card')
        else:
            messages.success(req,('There was an Error.'))
            return render(req,'addCard.html',{})


    return render(req,'addCard.html',{})

def card(req):
    all_cards = Card.objects.all
    return render(req,'card.html',{'all_cards':all_cards})

def reqYahoo(request):
    from app.tobecalled import reqYhaoo
    return render(request, "reqYhaoo.html", {'y': reqYhaoo()})

def edit(req,list_id):
    if req.method=='POST':
        current_card = Card.objects.get(pk=list_id)
        form=AddCard(req.POST or None, instance=current_card)
        if form.is_valid():
            form.save()
            messages.success(req,('Card has been edited'))
            return redirect('card')
        else:
            messages.success(req,('There was an Error.'))
            return render(req,'edit.html',{})
    else:
        get_card = Card.objects.get(pk=list_id)
        return render(req,'edit.html',{'get_card':get_card})

def delete(req,list_id):
    if req.method=='POST':
        current_card = Card.objects.get(pk=list_id)
        current_card.delete()
        messages.success(req,('Card has been delete'))
        return redirect('card')
    else:
        messages.success(req,('Nothing to see here'))
        return redirect('card')
