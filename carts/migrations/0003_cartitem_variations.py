# Generated by Django 5.0.1 on 2024-01-14 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("carts", "0002_rename_product_cartitem_product"),
        ("store", "0002_variation"),
    ]

    operations = [
        migrations.AddField(
            model_name="cartitem",
            name="variations",
            field=models.ManyToManyField(blank=True, to="store.variation"),
        ),
    ]