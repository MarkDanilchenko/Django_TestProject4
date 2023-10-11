from django.contrib import admin
from . import models


class CustomerAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Customer initials",
            {
                "fields": (
                    "name",
                    "surname",
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
    list_display = ("name", "surname", "email", "phone")
    search_fields = ("name", "surname")
    list_filter = ("name", "surname")


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
            "Seller initials",
            {
                "fields": (
                    "name",
                    "surname",
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
        (
            "Personal job info",
            {
                "fields": (
                    "date of employment",
                    "position",
                )
            },
        ),
    )
    list_display = (
        "name",
        "surname",
        "email",
        "phone",
        "position",
        "date_of_employment",
    )
    search_fields = ("name", "surname", "position", "date_of_employment")
    list_filter = ("name", "surname", "position", "date_of_employment")


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
                    "date_of_sale",
                )
            },
        ),
    )
    list_display = ("item", "date_of_sale")
    search_fields = ("item", "date_of_sale")
    list_filter = ("item", "date_of_sale")


admin.site.register(models.Sale, SaleAdmin)
