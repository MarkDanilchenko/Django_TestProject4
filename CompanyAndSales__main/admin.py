from django.contrib import admin
from . import models


class CustomerAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Customer credentials",
            {
                "fields": (
                    "firstName",
                    "lastName",
                )
            },
        ),
        (
            "Personal additional info",
            {
                "fields": (
                    "phone",
                    "email",
                )
            },
        ),
    )
    list_display = ("firstName", "lastName", "email", "phone")
    search_fields = ("firstName", "lastName", "email")
    list_filter = ("firstName", "lastName")


admin.site.register(models.Customer, CustomerAdmin)


class ItemAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Item name", {"fields": ("name",)}),
        ("Item description", {"fields": ("description",)}),
        ("Item price", {"fields": ("price",)}),
    )
    list_display = ("name", "description", "price")
    search_fields = ("name",)
    list_filter = ("name", "price")


admin.site.register(models.Item, ItemAdmin)


class SellerAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Seller credentials",
            {
                "fields": (
                    "firstName",
                    "lastName",
                )
            },
        ),
        (
            "Personal additional info",
            {
                "fields": (
                    "phone",
                    "email",
                    "dateOfEmployment",
                    "position",
                )
            },
        ),
    )
    list_display = (
        "firstName",
        "lastName",
        "email",
        "phone",
        "position",
        "dateOfEmployment",
    )
    search_fields = ("firstName", "lastName", "position")
    list_filter = ("firstName", "lastName", "position", "dateOfEmployment")


admin.site.register(models.Seller, SellerAdmin)


class SaleAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Sale details",
            {
                "fields": (
                    "item",
                    "seller",
                    "customer",
                    "dateOfSale",
                )
            },
        ),
    )
    list_display = ("item", "dateOfSale")
    search_fields = ("item",)
    list_filter = ("item", "dateOfSale")


admin.site.register(models.Sale, SaleAdmin)
