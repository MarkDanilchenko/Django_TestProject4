from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from . import models


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )


class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = ["name", "surname", "email", "phone"]

    name = forms.CharField(
        max_length=100,
        required=True,
        label="Customer name",
        help_text="Enter your name",
    )
    surname = forms.CharField(
        max_length=100,
        required=True,
        label="Customer surname",
        help_text="Enter your surname",
    )
    email = forms.EmailField(
        max_length=254,
        required=True,
        label="Customer email",
        help_text="Enter your email like test@test.com",
    )
    phone = forms.CharField(
        max_length=12,
        required=True,
        label="Customer phone",
        help_text="Enter your phone in the format +00000000000",
    )


class SellerForm(forms.ModelForm):
    class Meta:
        model = models.Seller
        fields = ["name", "surname", "email", "phone", "date_of_employment", "position"]

    name = forms.CharField(
        max_length=100, required=True, label="Seller name", help_text="Enter your name"
    )
    surname = forms.CharField(
        max_length=100,
        required=True,
        label="Seller surname",
        help_text="Enter your surname",
    )
    email = forms.EmailField(
        max_length=254,
        required=True,
        label="Seller email",
        help_text="Enter your email like test@test.com",
    )
    phone = forms.CharField(
        max_length=12,
        required=True,
        label="Seller phone",
        help_text="Enter your phone in the format +00000000000",
    )
    date_of_employment = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}),
        required=True,
        label="Date of employment",
        help_text="Enter seller's employment date",
    )
    position = forms.ChoiceField(
        required=True,
        choices=[
            ("Seller", "Seller"),
            ("Senior Manager", "Senior Manager"),
            ("Head of department", "Head of department"),
        ],
        label="Position",
        help_text="Enter seller's position",
    )


class ItemForm(forms.ModelForm):
    class Meta:
        model = models.Item
        fields = ["name", "description", "price"]

    name = forms.CharField(
        max_length=100,
        required=True,
        label="Item name",
        help_text="Enter item name",
    )

    description = forms.CharField(
        widget=forms.Textarea,
        required=True,
        label="Item description",
        help_text="Enter item description",
    )

    price = forms.FloatField(
        required=True,
        label="Item price",
        help_text="Enter item price, $",
    )


# class SaleForm(forms.ModelForm):
#     class Meta:
#         model = models.Sale
#         fields = ["item", "seller", "date_of_sale"]
