from django.urls import path, re_path, include
from django.views.generic import TemplateView
from . import views

urlpatterns_dbCategories = [
    path("DBcustomer", views.viewDBCustomer, name='viewDBCustomer'),
    path("DBcustomer/addCustomer", views.addCustomer, name='addCustomer'),
    re_path(r"DBcustomer/deleteCustomer/(?P<id>\d+)", views.deleteCustomer, name='deleteCustomer'),
    path('DBseller', views.viewDBSeller, name='viewDBSeller'),
    path('DBitem', views.viewDBItem, name='viewDBItem'),
    path('DBsale', views.viewDBSale, name='viewDBSale'),
]

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html")),
    path("DBCategories/", views.viewDBCategories, name='viewDBCategories'),
    path("DBCategories/", include(urlpatterns_dbCategories)),
]
