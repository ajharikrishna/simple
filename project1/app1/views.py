from django.shortcuts import render
from .models import SavingsAccount

# Create your views here.
def showIndex(request):
    return render(request,"index.html")


def save(request):
    return render(request,"web.html")




def viewaccount(request):
    view = SavingsAccount.objects.all()
    return render(request,"view.html",{"view":view})




def saveIndex(request):
    acno = request.POST.get("acno")
    name = request.POST.get("name")
    balance = request.POST.get("ob")
    password = request.POST.get("pw")

    sa = SavingsAccount(acno = acno,name=name,balance = balance,password = password)
    sa.save()

    return render(request,"index.html",{"message":"account created"})


