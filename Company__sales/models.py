import datetime
from django.core.exceptions import ValidationError
from django.core import validators
from django.db import models
import re


def phone_validator(value):
    pattern = r"^\+[0-9]{11}$"
    try:
        re.match(pattern, value).group()
        return value
    except:
        raise ValidationError("Enter phone in the format +00000000000")


def checkDate(value):
    if value > datetime.date.today():
        raise ValidationError(
            "Date cannot be in the future. Please enter a date in the past or current date."
        )
    else:
        return value


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
        validators=[phone_validator],
    )

    def __str__(self):
        return "%s %s;" % (self.name, self.surname)


class Item(models.Model):
    name = models.CharField(
        max_length=100, help_text="Enter name", unique=True, verbose_name="Item name"
    )
    description = models.TextField(
        help_text="Enter description", verbose_name="Item description"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Enter price, $",
        verbose_name="Price, $",
        default=0.00,
    )

    def __str__(self):
        return "Item|Price: %s | %s$;" % (self.name, self.price)


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
        max_length=12,
        help_text="Enter phone",
        unique=True,
        verbose_name="Seller phone",
        validators=[phone_validator],
    )
    date_of_employment = models.DateField(
        help_text="Enter date of employment",
        verbose_name="Seller date of employment",
        validators=[checkDate],
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
        return "%s %s - %s" % (self.name, self.surname, self.position)


class Sale(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_of_sale = models.DateField(
        help_text="Enter date of sale",
        verbose_name="Date of sale",
        validators=[checkDate],
    )

    def __str__(self):
        return "%s %s %s" % (self.item.name, self.item.price, self.date_of_sale)
