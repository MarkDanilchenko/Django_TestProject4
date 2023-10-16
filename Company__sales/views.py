from django.contrib.auth import authenticate, login
from django.db.models import Sum
from django.shortcuts import render, redirect
from . import forms, models
from . import my_funtions__reports
from fuzzywuzzy import process
from fuzzywuzzy import fuzz


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


# show all reports list
def viewDBReports(request):
    try:
        total_result = models.Sale.objects.all()
        if not total_result.exists():
            raise Exception
        else:
            return render(request, "DBReport_/DBReports.html")
    except:
        empty_result = """Reports are <span style='color: rgb(223, 14, 14);'>not available</span> now.<br> 
        Please, add any information to the \"Sales\" table in the database."""
        return render(
            request, "DBReport_/DBReports.html", {"empty_result": empty_result}
        )


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


# Reports functions
# Report 1
def viewDBReport_1(request):
    nameSurname__seller_userInput = request.GET.get("nameSurname__seller_report1")
    nameSurname__seller_DBlist = my_funtions__reports.report1__nameSurname__seller()
    if len(nameSurname__seller_userInput) > 0:
        result = process.extractOne(
            str(nameSurname__seller_userInput), nameSurname__seller_DBlist
        )
    if result[1] <= 60:
        return render(
            request,
            "DBreport_/report_1.html",
            {
                "result_notFound": "<span style='color: rgb(223, 14, 14);'>No</span> such seller. Clarify your request and try again."
            },
        )
    else:
        name = result[0].split(" ")[0]
        surname = result[0].split(" ")[1]
        result = models.Sale.objects.filter(seller__name=name, seller__surname=surname)
        return render(
            request,
            "DBreport_/report_1.html",
            {"result": result, "search_name": name, "search_surname": surname},
        )


# Report 2
def viewDBReport_2(request):
    try:
        date_userInput = request.GET.get("date_report2")
        result = models.Sale.objects.filter(date_of_sale=date_userInput)
        if not result.exists():
            raise Exception
        else:
            return render(request, "DBreport_/report_2.html", {"result": result})
    except:
        result_notFound = "<span style='color: rgb(223, 14, 14);'>No</span> any sales on this date. Clarify your request and try again."
        return render(
            request, "DBreport_/report_2.html", {"result_notFound": result_notFound}
        )


# Report 3
def viewDBReport_3(request):
    itemName_userInput = request.GET.get("item_report3")
    itemName_DBlist = my_funtions__reports.report3__itemName()
    if len(itemName_userInput) > 0:
        result = process.extractOne(str(itemName_userInput), itemName_DBlist)
    if result[1] <= 60:
        return render(
            request,
            "DBreport_/report_3.html",
            {
                "result_notFound": "<span style='color: rgb(223, 14, 14);'>No</span> of these items were sold. Clarify your request and try again."
            },
        )
    else:
        searchedItem = models.Item.objects.get(name=result[0])
        result = searchedItem.sale_set.all()
        return render(request, "DBreport_/report_3.html", {"result": result})


#  Report 4
def viewDBReport_4(request):
    try:
        date_userInput = request.GET.get("date_report4")
        result = models.Sale.objects.filter(date_of_sale=date_userInput)
        if not result.exists():
            raise Exception
        else:
            result_sum = models.Sale.objects.filter(
                date_of_sale=date_userInput
            ).aggregate(Sum("item__price"))["item__price__sum"]

            result_count = models.Sale.objects.filter(
                date_of_sale=date_userInput
            ).count()

            return render(
                request,
                "DBreport_/report_4.html",
                {
                    "date_userInput": date_userInput,
                    "result_count": result_count,
                    "result_sum": result_sum,
                },
            )
    except:
        result_notFound = "<span style='color: rgb(223, 14, 14);'>No</span> any sales on this date. Clarify your request and try again."
        return render(
            request, "DBreport_/report_4.html", {"result_notFound": result_notFound}
        )
