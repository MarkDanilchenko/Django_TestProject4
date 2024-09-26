from django.urls import path, re_path, include
from django.views.generic import TemplateView
from . import views

urlpatterns_categories = [
    path("customers", views.getCustomers, name="getCustomers"),
    path("customers/addCustomer", views.addCustomer, name="addCustomer"),
    re_path(
        r"customers/editCustomer/(?P<id>\d+)", views.editCustomer, name="editCustomer"
    ),
    re_path(
        r"customers/deleteCustomer/(?P<id>\d+)",
        views.deleteCustomer,
        name="deleteCustomer",
    ),
    path("sellers", views.getSellers, name="getSellers"),
    path("sellers/addSeller", views.addSeller, name="addSeller"),
    re_path(r"sellers/editSeller/(?P<id>\d+)", views.editSeller, name="editSeller"),
    re_path(
        r"sellers/deleteSeller/(?P<id>\d+)", views.deleteSeller, name="deleteSeller"
    ),
    path("items", views.getItems, name="getItems"),
    path("items/addItem", views.addItem, name="addItem"),
    re_path(r"items/editItem/(?P<id>\d+)", views.editItem, name="editItem"),
    re_path(r"items/deleteItem/(?P<id>\d+)", views.deleteItem, name="deleteItem"),
    path("sales", views.getSales, name="getSales"),
    path("sales/addSale", views.addSale, name="addSale"),
    re_path(r"sales/editSale/(?P<id>\d+)", views.editSale, name="editSale"),
    re_path(r"sales/deleteSale/(?P<id>\d+)", views.deleteSale, name="deleteSale"),
]

urlpatterns_reports = [
    path("report_1", views.createReport_1, name="createReport_1"),
    path("report_2", views.createReport_2, name="createReport_2"),
    path("report_3", views.createReport_3, name="createReport_3"),
    path("report_4", views.createReport_4, name="createReport_4"),
    path("report_5", views.createReport_5, name="createReport_5"),
    path("report_6", views.createReport_6, name="createReport_6"),
    path("report_7", views.createReport_7, name="createReport_7"),
    path("report_8", views.createReport_8, name="createReport_8"),
    path("report_9", views.createReport_9, name="createReport_9"),
    path("report_10", views.createReport_10, name="createReport_10"),
]

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html")),
    path("categories/", views.getCategories, name="getCategories"),
    path("categories/", include(urlpatterns_categories)),
    path("reports/", views.getReports, name="getReports"),
    path("reports/", include(urlpatterns_reports)),
]
