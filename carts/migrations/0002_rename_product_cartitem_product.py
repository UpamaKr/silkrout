# Generated by Django 4.2 on 2024-01-14 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("carts", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cartitem",
            old_name="Product",
            new_name="product",
        ),
    ]