import datetime
from django.core.exceptions import ValidationError
from django.db import models


class Customer(models.Model):
    name = models.CharField(
        max_length=100, help_text="Enter name", verbose_name="Customer name"
    )
    surname = models.CharField(
        max_length=100, help_text="Enter surname", verbose_name="Customer surname"
    )
    email = models.EmailField(
        help_text="Enter email", unique=True, verbose_name="Customer email"
    )
    phone = models.CharField(
        max_length=12,
        help_text="Enter phone",
        unique=True,
        verbose_name="Customer phone",
    )

    def __str__(self):
        return self.name, self.surname, self.email


class Item(models.Model):
    name = models.CharField(
        max_length=100, help_text="Enter name", unique=True, verbose_name="Item name"
    )
    description = models.TextField(
        help_text="Enter description", verbose_name="Item description"
    )

    def __str__(self):
        return self.name


class Seller(models.Model):
    name = models.CharField(
        max_length=100, help_text="Enter name", verbose_name="Seller name"
    )
    surname = models.CharField(
        max_length=100, help_text="Enter surname", verbose_name="Seller surname"
    )
    email = models.EmailField(
        help_text="Enter email", unique=True, verbose_name="Seller email"
    )
    phone = models.CharField(
        max_length=12, help_text="Enter phone", unique=True, verbose_name="Seller phone"
    )
    date_of_employment = models.DateField(
        help_text="Enter date of employment", verbose_name="Seller date of employment"
    )
    choices = [
        ("Seller", "Seller"),
        ("Senior Manager", "Senior Manager"),
        ("Head of department", "Head of department"),
    ]
    position = models.CharField(
        max_length=100,
        choices=choices,
        help_text="Enter position",
        verbose_name="Seller position",
    )

    def __str__(self):
        return self.name, self.surname, self.position


def checkDate(value):
    if value > datetime.datetime.today():
        raise ValidationError(
            "Date cannot be in the future. Please enter a date in the past or current date."
        )
    else:
        return value


class Sale(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_of_sale = models.DateField(
        help_text="Enter date of sale",
        verbose_name="Date of sale",
        validators=[checkDate],
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Enter price", verbose_name="Price", default=0.00)
