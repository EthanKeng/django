from django.shortcuts import render, redirect

# Create your views here.
def home(req):
    return render(req,'home.html',{})


def about(request):
    from app.tobecalled import generateArry
    return render(request, "about.html", {'list': generateArry()})

def addAdress(req):
    return render(req,'addAdress.html',{})

def reqYahoo(request):
    from app.tobecalled import reqYhaoo
    return render(request, "reqYhaoo.html", {'y': reqYhaoo()})
