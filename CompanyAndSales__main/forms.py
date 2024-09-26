from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from . import models


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

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
        fields = ["firstName", "lastName", "email", "phone"]

    firstName = forms.CharField(
        max_length=100,
        required=True,
        label="FirstName",
        help_text="Enter your firstName",
    )
    lastName = forms.CharField(
        max_length=100,
        required=True,
        label="LastName",
        help_text="Enter your lastName",
    )
    email = forms.EmailField(
        required=True,
        label="Email",
        help_text="email@example.com",
    )
    phone = forms.CharField(
        max_length=12,
        required=True,
        label="Phone",
        help_text="Enter your phone in the format +00000000000",
    )


class SellerForm(forms.ModelForm):
    class Meta:
        model = models.Seller
        fields = [
            "firstName",
            "lastName",
            "email",
            "phone",
            "dateOfEmployment",
            "position",
        ]

    firstName = forms.CharField(
        max_length=100,
        required=True,
        label="FirstName",
        help_text="Enter your firstName",
    )
    lastName = forms.CharField(
        max_length=100,
        required=True,
        label="LastName",
        help_text="Enter your lastName",
    )
    email = forms.EmailField(
        required=True,
        label="Email",
        help_text="email@example.com",
    )
    phone = forms.CharField(
        max_length=12,
        required=True,
        label="Phone",
        help_text="Enter your phone in the format +00000000000",
    )
    dateOfEmployment = forms.DateField(
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        required=True,
        label="Date of employment",
        help_text="Enter employment date",
    )
    position = forms.ChoiceField(
        required=True,
        choices=[
            ("Seller", "Seller"),
            ("Senior Manager", "Senior Manager"),
            ("Head of department", "Head of department"),
        ],
        label="Position",
        help_text="Enter position",
    )


class ItemForm(forms.ModelForm):
    class Meta:
        model = models.Item
        fields = ["name", "description", "price"]

    name = forms.CharField(
        max_length=100,
        required=True,
        label="Name",
        help_text="Enter item name",
    )

    description = forms.CharField(
        widget=forms.Textarea,
        required=True,
        label="Description",
        help_text="Enter item description",
    )

    price = forms.FloatField(
        required=True,
        label="Price",
        help_text="Enter item price, $",
    )


class SaleForm(forms.ModelForm):
    class Meta:
        model = models.Sale
        fields = ["item", "seller", "customer", "dateOfSale"]

    item = forms.ModelChoiceField(
        queryset=models.Item.objects.all(),
        required=True,
        label="Item",
        help_text="Select item",
    )

    seller = forms.ModelChoiceField(
        queryset=models.Seller.objects.all(),
        required=True,
        label="Seller",
        help_text="Select seller",
    )

    customer = forms.ModelChoiceField(
        queryset=models.Customer.objects.all(),
        required=True,
        label="Customer",
        help_text="Select customer",
    )

    dateOfSale = forms.DateField(
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        required=True,
        label="Date of sale",
        help_text="Enter date of sale",
    )
