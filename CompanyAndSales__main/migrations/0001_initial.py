# Generated by Django 4.2.6 on 2024-10-05 19:29

import CompanyAndSales__main.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "firstName",
                    models.CharField(
                        help_text="FirstName", max_length=100, verbose_name="FirstName"
                    ),
                ),
                (
                    "lastName",
                    models.CharField(
                        help_text="LastName", max_length=100, verbose_name="LastName"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        help_text="Email",
                        max_length=254,
                        unique=True,
                        verbose_name="Email",
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        help_text="Phone",
                        max_length=12,
                        unique=True,
                        validators=[CompanyAndSales__main.models.phone_validator],
                        verbose_name="Phone",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Name",
                        max_length=100,
                        unique=True,
                        verbose_name="Name",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Description", verbose_name="Description"
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        help_text="Price, $",
                        max_digits=10,
                        verbose_name="Price, $",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Seller",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "firstName",
                    models.CharField(
                        help_text="FirstName", max_length=100, verbose_name="FirstName"
                    ),
                ),
                (
                    "lastName",
                    models.CharField(
                        help_text="LastName", max_length=100, verbose_name="LastName"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        help_text="Email",
                        max_length=254,
                        unique=True,
                        verbose_name="Email",
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        help_text="Phone",
                        max_length=12,
                        unique=True,
                        validators=[CompanyAndSales__main.models.phone_validator],
                        verbose_name="Phone",
                    ),
                ),
                (
                    "dateOfEmployment",
                    models.DateField(
                        help_text="Date of employment",
                        validators=[CompanyAndSales__main.models.checkDate],
                        verbose_name="Date of employment",
                    ),
                ),
                (
                    "position",
                    models.CharField(
                        choices=[
                            ("Seller", "Seller"),
                            ("Senior Manager", "Senior Manager"),
                            ("Head of department", "Head of department"),
                        ],
                        help_text="Position",
                        max_length=100,
                        verbose_name="Position",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Sale",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "dateOfSale",
                    models.DateField(
                        help_text="Date of sale",
                        validators=[CompanyAndSales__main.models.checkDate],
                        verbose_name="Date of sale",
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="CompanyAndSales__main.customer",
                    ),
                ),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="CompanyAndSales__main.item",
                    ),
                ),
                (
                    "seller",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="CompanyAndSales__main.seller",
                    ),
                ),
            ],
        ),
    ]
