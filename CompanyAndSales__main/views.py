from django.contrib.auth import authenticate, login
from django.db.models import Sum, Count
from django.shortcuts import render, redirect
from . import forms, models


def signUp(request):
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
    return render(request, "registration/signup.html", {"form": form})


def getCategories(request):
    return render(request, "categories.html")


def getReports(request):
    try:
        sales = models.Sale.objects.all()
        if not sales.exists():
            raise Exception

        return render(request, "reports/reports.html")
    except:
        notFound = """
        Reports <span style='color: rgb(223, 14, 14);'>not found.</span><br> 
        Please, add any information to the \"Sales\" table in the database.
        """

        return render(request, "reports/reports.html", {"notFound": notFound})


def getCustomers(request):
    try:
        customers = models.Customer.objects.all()
        if not customers.exists():
            raise Exception

        return render(request, "dataCustomers.html", {"customers": customers})
    except Exception:
        notFound = """
        Customers <span style='color: rgb(223, 14, 14);'>not found.</span><br> Please add any customer information first.
        """

        return render(request, "dataCustomers.html", {"notFound": notFound})


def addCustomer(request):
    form = forms.CustomerForm()
    if request.method == "POST":
        form = forms.CustomerForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("/categories/customers")

    return render(request, "addCustomer.html", {"form": form})


def deleteCustomer(request, id):
    if models.Customer.objects.filter(id=id).exists():
        models.Customer.objects.get(id=id).delete()

    return redirect("/categories/customers")


def editCustomer(request, id):
    customer = models.Customer.objects.get(id=id)
    form = forms.CustomerForm(instance=customer)
    if request.method == "POST":
        form = forms.CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()

            return redirect("/categories/customers")

    return render(request, "editCustomer.html", {"form": form})


def getSellers(request):
    try:
        sellers = models.Seller.objects.all()
        if not sellers.exists():
            raise Exception

        return render(request, "dataSellers.html", {"sellers": sellers})
    except Exception:
        notFound = """
        Sellers <span style='color: rgb(223, 14, 14);'>not found.</span><br> Please add any seller information first.
        """

        return render(request, "dataSellers.html", {"notFound": notFound})


def addSeller(request):
    form = forms.SellerForm()
    if request.method == "POST":
        form = forms.SellerForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("/categories/sellers")

    return render(request, "addSeller.html", {"form": form})


def deleteSeller(request, id):
    if models.Seller.objects.filter(id=id).exists():
        models.Seller.objects.get(id=id).delete()

    return redirect("/categories/sellers")


def editSeller(request, id):
    seller = models.Seller.objects.get(id=id)
    form = forms.SellerForm(instance=seller)
    if request.method == "POST":
        form = forms.SellerForm(request.POST, instance=seller)
        if form.is_valid():
            form.save()

            return redirect("/categories/sellers")

    return render(request, "editSeller.html", {"form": form})


def getItems(request):
    try:
        items = models.Item.objects.all()
        if not items.exists():
            raise Exception

        return render(request, "dataItems.html", {"items": items})
    except Exception:
        notFound = """
        Items <span style='color: rgb(223, 14, 14);'>not found.</span><br> Please add any item information first.
        """

        return render(request, "dataItems.html", {"notFound": notFound})


def addItem(request):
    form = forms.ItemForm()
    if request.method == "POST":
        form = forms.ItemForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("/categories/items")

    return render(request, "addItem.html", {"form": form})


def deleteItem(request, id):
    if models.Item.objects.filter(id=id).exists():
        models.Item.objects.get(id=id).delete()

    return redirect("/categories/items")


def editItem(request, id):
    item = models.Item.objects.get(id=id)
    form = forms.ItemForm(instance=item)
    if request.method == "POST":
        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()

            return redirect("/categories/items")

    return render(request, "editItem.html", {"form": form})


def getSales(request):
    try:
        sales = models.Sale.objects.all()
        if not sales.exists():
            raise Exception

        return render(request, "dataSales.html", {"sales": sales})
    except Exception:
        notFound = """
        Sales <span style='color: rgb(223, 14, 14);'>not found.</span><br><br> Please add any sale information first.
        """

        return render(request, "dataSales.html", {"notFound": notFound})


def addSale(request):
    form = forms.SaleForm()
    if request.method == "POST":
        form = forms.SaleForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("/categories/sales")

    return render(request, "addSale.html", {"form": form})


def deleteSale(request, id):
    if models.Sale.objects.filter(id=id).exists():
        models.Sale.objects.get(id=id).delete()

    return redirect("/categories/sales")


def editSale(request, id):
    sale = models.Sale.objects.get(id=id)
    form = forms.SaleForm(instance=sale)
    if request.method == "POST":
        form = forms.SaleForm(request.POST, instance=sale)
        if form.is_valid():
            form.save()

            return redirect("/categories/sales")

    return render(request, "editSale.html", {"form": form})


def createReport_1(request):
    sellerId_report_1 = request.GET.get("sellerId_report_1")

    if not models.Seller.objects.filter(id=sellerId_report_1).exists():
        return render(
            request,
            "reports/report_1.html",
            {
                "notFound": "Seller <span style='color: rgb(223, 14, 14);'>not found.</span>"
            },
        )

    seller = models.Seller.objects.get(id=sellerId_report_1)
    sellerFirstName = seller.firstName
    sellerLastName = seller.lastName

    relatedSales = models.Sale.objects.filter(
        seller__firstName=sellerFirstName, seller__lastName=sellerLastName
    )

    return render(
        request,
        "reports/report_1.html",
        {
            "relatedSales": relatedSales,
            "sellerFirstName": sellerFirstName,
            "sellerLastName": sellerLastName,
        },
    )


def createReport_2(request):
    date_report_2 = request.GET.get("date_report_2")

    sales = models.Sale.objects.filter(dateOfSale=date_report_2)
    if not sales.exists():
        notFound = """
        <span style='color: rgb(223, 14, 14);'>No</span> any sales on this date.
        """

        return render(request, "reports/report_2.html", {"notFound": notFound})

    return render(request, "reports/report_2.html", {"sales": sales})


def createReport_3(request):
    itemName_report_3 = request.GET.get("itemName_report_3")

    if not models.Item.objects.filter(name=itemName_report_3).exists():
        return render(
            request,
            "reports/report_3.html",
            {
                "notFound": "Item <span style='color: rgb(223, 14, 14);'>not found.</span>"
            },
        )

    relatedSales = models.Sale.objects.filter(item__name=itemName_report_3)

    return render(
        request,
        "reports/report_3.html",
        {"relatedSales": relatedSales, "itemName_report_3": itemName_report_3},
    )


def createReport_4(request):
    date_report_4 = request.GET.get("date_report_4")

    sales = models.Sale.objects.filter(dateOfSale=date_report_4)
    if not sales.exists():
        notFound = """
        <span style='color: rgb(223, 14, 14);'>No</span> any sales on this date.
        """

        return render(request, "reports/report_4.html", {"notFound": notFound})

    totalSalesSum = sales.aggregate(Sum("item__price"))["item__price__sum"]
    totalSalesCount = sales.count()

    return render(
        request,
        "reports/report_4.html",
        {
            "date_report_4": date_report_4,
            "totalSalesCount": totalSalesCount,
            "totalSalesSum": totalSalesSum,
        },
    )


def createReport_5(request):
    salesCounted = list(
        models.Sale.objects.values("item__name")
        .annotate(amount=Count("item__name"))
        .order_by("-amount")
    )

    maxSoldAmount = salesCounted[0]["amount"]
    topSoldItems = list(filter(lambda x: x["amount"] == maxSoldAmount, salesCounted))

    return render(
        request,
        "reports/report_5.html",
        {"topSoldItems": topSoldItems},
    )


def createReport_6(request):
    salesSummed = (
        models.Sale.objects.values("seller__firstName", "seller__lastName")
        .annotate(totalSum=Sum("item__price"))
        .order_by("-totalSum")
        .first()
    )

    topSellerFirstName = salesSummed["seller__firstName"]
    topSellerLastName = salesSummed["seller__lastName"]
    topSellerTotalSum = salesSummed["totalSum"]

    return render(
        request,
        "reports/report_6.html",
        {
            "topSellerFirstName": topSellerFirstName,
            "topSellerLastName": topSellerLastName,
            "topSellerTotalSum": topSellerTotalSum,
        },
    )


def createReport_7(request):
    salesSummed = (
        models.Sale.objects.values("customer__firstName", "customer__lastName")
        .annotate(totalSum=Sum("item__price"))
        .order_by("-totalSum")
        .first()
    )

    topCustomerFirstName = salesSummed["customer__firstName"]
    topCustomerLastName = salesSummed["customer__lastName"]
    topCustomerTotalSum = salesSummed["totalSum"]

    return render(
        request,
        "reports/report_7.html",
        {
            "topCustomerFirstName": topCustomerFirstName,
            "topCustomerLastName": topCustomerLastName,
            "topCustomerTotalSum": topCustomerTotalSum,
        },
    )


def createReport_8(request):
    dateStart_report_8 = request.GET.get("dateStart_report_8")
    dateEnd_report_8 = request.GET.get("dateEnd_report_8")

    salesInDateRange = models.Sale.objects.filter(
        dateOfSale__range=[dateStart_report_8, dateEnd_report_8]
    )

    if not salesInDateRange:
        notFound = (
            "<span style='color: rgb(223, 14, 14);'>No</span> any sales on this period."
        )

        return render(request, "reports/report_8.html", {"notFound": notFound})

    salesInDateRangeCounted = (
        salesInDateRange.values("item__name")
        .annotate(amount=Count("item__name"))
        .order_by("-amount")
    )
    maxSalesAmountInDateRange = salesInDateRangeCounted[0]["amount"]
    topSalesItemsInDateRange = list(
        filter(
            lambda x: x["amount"] == maxSalesAmountInDateRange, salesInDateRangeCounted
        )
    )

    return render(
        request,
        "reports/report_8.html",
        {
            "dateStart_report_8": dateStart_report_8,
            "dateEnd_report_8": dateEnd_report_8,
            "topSalesItemsInDateRange": topSalesItemsInDateRange,
        },
    )


def createReport_9(request):
    dateStart_report_9 = request.GET.get("dateStart_report_9")
    dateEnd_report_9 = request.GET.get("dateEnd_report_9")

    salesInDateRange = models.Sale.objects.filter(
        dateOfSale__range=[dateStart_report_9, dateEnd_report_9]
    )

    if not salesInDateRange:
        notFound = (
            "<span style='color: rgb(223, 14, 14);'>No</span> any sales on this period."
        )

        return render(request, "reports/report_9.html", {"notFound": notFound})

    sellersStatsInDateRange = (
        salesInDateRange.values("seller__firstName", "seller__lastName")
        .annotate(totalSum=Sum("item__price"))
        .order_by("-totalSum")
    )
    maxProfitInDateRange = sellersStatsInDateRange[0]["totalSum"]
    topProfitSellersInDateRange = list(
        filter(lambda x: x["totalSum"] == maxProfitInDateRange, sellersStatsInDateRange)
    )

    return render(
        request,
        "reports/report_9.html",
        {
            "dateStart_report_9": dateStart_report_9,
            "dateEnd_report_9": dateEnd_report_9,
            "topProfitSellersInDateRange": topProfitSellersInDateRange,
        },
    )


def createReport_10(request):
    dateStart_report_10 = request.GET.get("dateStart_report_10")
    dateEnd_report_10 = request.GET.get("dateEnd_report_10")

    salesInDateRange = models.Sale.objects.filter(
        dateOfSale__range=[dateStart_report_10, dateEnd_report_10]
    )

    if not salesInDateRange:
        notFound = (
            "<span style='color: rgb(223, 14, 14);'>No</span> any sales on this period."
        )

        return render(request, "reports/report_10.html", {"notFound": notFound})

    customersStatsInDateRange = (
        salesInDateRange.values("customer__firstName", "customer__lastName")
        .annotate(totalSum=Sum("item__price"))
        .order_by("-totalSum")
    )
    maxProfitInDateRange = customersStatsInDateRange[0]["totalSum"]
    topProfitCustomersInDateRange = list(
        filter(
            lambda x: x["totalSum"] == maxProfitInDateRange, customersStatsInDateRange
        )
    )

    return render(
        request,
        "reports/report_10.html",
        {
            "dateStart_report_10": dateStart_report_10,
            "dateEnd_report_10": dateEnd_report_10,
            "topProfitCustomersInDateRange": topProfitCustomersInDateRange,
        },
    )
