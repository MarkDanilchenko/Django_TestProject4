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
        empty_result = "Customers' data is <span style='color: rgb(223, 14, 14);'>empty.</span><br><br> Please add any customer information first."
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


def editCustomer(request, id):
    customer = models.Customer.objects.get(id=id)
    form = forms.CustomerForm(instance=customer)
    if request.method == "POST":
        form = forms.CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("/DBCategories/DBcustomer")
    return render(request, "editCustomer.html", {"form": form})


# Seller functions
def viewDBSeller(request):
    try:
        result = models.Seller.objects.all()
        if not result.exists():
            raise Exception
        else:
            return render(request, "DBseller_data.html", {"result": result})
    except Exception:
        empty_result = "Sellers' data is <span style='color: rgb(223, 14, 14);'>empty.</span><br><br> Please add any seller information first."
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


def editSeller(request, id):
    seller = models.Seller.objects.get(id=id)
    form = forms.SellerForm(instance=seller)
    if request.method == "POST":
        form = forms.SellerForm(request.POST, instance=seller)
        if form.is_valid():
            form.save()
            return redirect("/DBCategories/DBseller")
    return render(request, "editSeller.html", {"form": form})


# Item functions
def viewDBItem(request):
    try:
        result = models.Item.objects.all()
        if not result.exists():
            raise Exception
        else:
            return render(request, "DBitem_data.html", {"result": result})
    except Exception:
        empty_result = "Items' data is <span style='color: rgb(223, 14, 14);'>empty.</span><br><br> Please add any item information first."
        return render(request, "DBitem_data.html", {"empty_result": empty_result})


def addItem(request):
    form = forms.ItemForm()
    if request.method == "POST":
        form = forms.ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/DBCategories/DBitem")

    return render(request, "addItem.html", {"form": form})


def deleteItem(request, id):
    try:
        if models.Item.objects.filter(id=id).exists():
            models.Item.objects.get(id=id).delete()
        return redirect("/DBCategories/DBitem")
    except:
        return redirect("/DBCategories/DBitem")


def editItem(request, id):
    item = models.Item.objects.get(id=id)
    form = forms.ItemForm(instance=item)
    if request.method == "POST":
        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("/DBCategories/DBitem")
    return render(request, "editItem.html", {"form": form})


# Sales functions
def viewDBSale(request):
    try:
        result = models.Sale.objects.all()
        if not result.exists():
            raise Exception
        else:
            return render(request, "DBsale_data.html", {"result": result})
    except Exception:
        empty_result = "Sales' data is <span style='color: rgb(223, 14, 14);'>empty.</span><br><br> Please add any sale information first."
        return render(request, "DBsale_data.html", {"empty_result": empty_result})


def addSale(request):
    form = forms.SaleForm()
    if request.method == "POST":
        form = forms.SaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/DBCategories/DBsale")

    return render(request, "addSale.html", {"form": form})


def deleteSale(request, id):
    try:
        if models.Sale.objects.filter(id=id).exists():
            models.Sale.objects.get(id=id).delete()
        return redirect("/DBCategories/DBsale")
    except:
        return redirect("/DBCategories/DBsale")


def editSale(request, id):
    sale = models.Sale.objects.get(id=id)
    form = forms.SaleForm(instance=sale)
    if request.method == "POST":
        form = forms.SaleForm(request.POST, instance=sale)
        if form.is_valid():
            form.save()
            return redirect("/DBCategories/DBsale")
    return render(request, "editSale.html", {"form": form})
