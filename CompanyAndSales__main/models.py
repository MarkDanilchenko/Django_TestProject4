import datetime
import re
from django.core.exceptions import ValidationError
from django.db import models


def phone_validator(value):
    pattern = r"^\+[0-9]{11}$"
    try:
        re.match(pattern, value).group()

        return value
    except:
        raise ValidationError("Phone should be in the format: +00000000000")


def checkDate(value):
    if value > datetime.date.today():
        raise ValidationError("Invalid date.")

    return value


class Customer(models.Model):
    firstName = models.CharField(
        max_length=100, help_text="FirstName", verbose_name="FirstName"
    )
    lastName = models.CharField(
        max_length=100, help_text="LastName", verbose_name="LastName"
    )
    email = models.EmailField(help_text="Email", unique=True, verbose_name="Email")
    phone = models.CharField(
        max_length=12,
        help_text="Phone",
        unique=True,
        verbose_name="Phone",
        validators=[phone_validator],
    )

    def __str__(self):
        return f"{self.firstName} {self.lastName}"


class Item(models.Model):
    name = models.CharField(
        max_length=100, help_text="Name", unique=True, verbose_name="Name"
    )
    description = models.TextField(help_text="Description", verbose_name="Description")
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Price, $",
        verbose_name="Price, $",
        default=0.00,
    )

    def __str__(self):
        return f"{self.name}"


class Seller(models.Model):
    firstName = models.CharField(
        max_length=100, help_text="FirstName", verbose_name="FirstName"
    )
    lastName = models.CharField(
        max_length=100, help_text="LastName", verbose_name="LastName"
    )
    email = models.EmailField(help_text="Email", unique=True, verbose_name="Email")
    phone = models.CharField(
        max_length=12,
        help_text="Phone",
        unique=True,
        verbose_name="Phone",
        validators=[phone_validator],
    )
    dateOfEmployment = models.DateField(
        help_text="Date of employment",
        verbose_name="Date of employment",
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
        help_text="Position",
        verbose_name="Position",
    )

    def __str__(self):
        return f"{self.firstName} {self.lastName}"


class Sale(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    dateOfSale = models.DateField(
        help_text="Date of sale",
        verbose_name="Date of sale",
        validators=[checkDate],
    )

    def __str__(self):
        return f"{self.item.name} {self.item.price} {self.dateOfSale}"
