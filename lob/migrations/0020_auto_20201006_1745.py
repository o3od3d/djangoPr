# Generated by Django 3.1 on 2020-10-06 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lob', '0019_basket_food_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Basket',
        ),
        migrations.DeleteModel(
            name='Food',
        ),
    ]