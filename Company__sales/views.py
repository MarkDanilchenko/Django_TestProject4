from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from . import forms, models


# user registartion
def registration(request):
    if request.method == "POST":
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("/")
    else:
        form = forms.UserRegisterForm()
    return render(request, "registration/registration.html", {"form": form})


# show all categories
def viewDBCategories(request):
    return render(request, "DBCategories.html")


# Customer functions
def viewDBCustomer(request):
    try:
        result = models.Customer.objects.all()
        if not result.exists():
            raise Exception
        else:
            return render(request, "DBcustomer_data.html", {"result": result})
    except Exception:
        empty_result = "Customers's data is <span style='color: rgb(223, 14, 14);'>empty.</span><br><br> Please add any customer information first."
        return render(request, "DBcustomer_data.html", {"empty_result": empty_result})


def addCustomer(request):
    form = forms.CustomerForm()
    if request.method == "POST":
        form = forms.CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/DBCategories/DBcustomer")

    return render(request, "addCustomer.html", {"form": form})


def deleteCustomer(request, id):
    try:
        if models.Customer.objects.filter(id=id).exists():
            models.Customer.objects.get(id=id).delete()
        return redirect("/DBCategories/DBcustomer")
    except:
        return redirect("/DBCategories/DBcustomer")


# Seller functions
def viewDBSeller(request):
    try:
        result = models.Seller.objects.all()
        if not result.exists():
            raise Exception
        else:
            return render(request, "DBseller_data.html", {"result": result})
    except Exception:
        empty_result = "Sellers's data is <span style='color: rgb(223, 14, 14);'>empty.</span><br><br> Please add any seller information first."
        return render(request, "DBseller_data.html", {"empty_result": empty_result})


def addSeller(request):
    form = forms.SellerForm()
    if request.method == "POST":
        form = forms.SellerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/DBCategories/DBseller")

    return render(request, "addSeller.html", {"form": form})


def deleteSeller(request, id):
    try:
        if models.Seller.objects.filter(id=id).exists():
            models.Seller.objects.get(id=id).delete()
        return redirect("/DBCategories/DBseller")
    except:
        return redirect("/DBCategories/DBseller")


# Item functions
def viewDBItem(request):
    return render(request, "DBitem_data.html")


# Sales functions
def viewDBSale(request):
    return render(request, "DBsale_data.html")
