# Generated by Django 3.0.3 on 2020-07-03 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CommodityApp', '0004_commodities_breed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commodities',
            old_name='priceforbulk',
            new_name='priceperkg',
        ),
        migrations.RenameField(
            model_name='commodities',
            old_name='priceperunit',
            new_name='priceperquintal',
        ),
    ]