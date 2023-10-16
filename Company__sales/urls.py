from django.urls import path, re_path, include
from django.views.generic import TemplateView
from . import views

urlpatterns_dbCategories = [
    path("DBcustomer", views.viewDBCustomer, name='viewDBCustomer'),
    path("DBcustomer/addCustomer", views.addCustomer, name='addCustomer'),
    re_path(r"DBcustomer/editCustomer/(?P<id>\d+)", views.editCustomer, name='editCustomer'),
    re_path(r"DBcustomer/deleteCustomer/(?P<id>\d+)", views.deleteCustomer, name='deleteCustomer'),
    # 
    path('DBseller', views.viewDBSeller, name='viewDBSeller'),
    path('DBseller/addSeller', views.addSeller, name='addSeller'),
    re_path(r"DBseller/editSeller/(?P<id>\d+)", views.editSeller, name='editSeller'),
    re_path(r"DBseller/deleteSeller/(?P<id>\d+)", views.deleteSeller, name='deleteSeller'),
    # 
    path('DBitem', views.viewDBItem, name='viewDBItem'),
    path('DBitem/addItem', views.addItem, name='addItem'),
    re_path(r"DBitem/editItem/(?P<id>\d+)", views.editItem, name='editItem'),
    re_path(r"DBitem/deleteItem/(?P<id>\d+)", views.deleteItem, name='deleteItem'),
    # 
    path('DBsale', views.viewDBSale, name='viewDBSale'),
    path('DBsale/addSale', views.addSale, name='addSale'),
    re_path(r"DBsale/editSale/(?P<id>\d+)", views.editSale, name='editSale'),
    re_path(r"DBsale/deleteSale/(?P<id>\d+)", views.deleteSale, name='deleteSale'),
    # 
]

urlpatterns_dbReports = [
    path('DBReport_1', views.viewDBReport_1, name='viewDBReport_1'),
    path('DBReport_2', views.viewDBReport_2, name='viewDBReport_2'),
    path('DBReport_3', views.viewDBReport_3, name='viewDBReport_3'),
    path('DBReport_4', views.viewDBReport_4, name='viewDBReport_4'),
]

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html")),
    # 
    path("DBCategories/", views.viewDBCategories, name='viewDBCategories'),
    path("DBCategories/", include(urlpatterns_dbCategories)),
    # 
    path('DBReports/', views.viewDBReports, name='viewDBReports'),
    path('DBReports/', include(urlpatterns_dbReports)),
    # 
]
