# Generated by Django 3.0.6 on 2020-07-04 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CommodityApp', '0013_order_perishable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='perishable',
        ),
        migrations.AddField(
            model_name='commodities',
            name='perishable',
            field=models.BooleanField(default=False),
        ),
    ]