# Generated by Django 3.0.6 on 2020-07-04 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeliverySystem', '0009_truckorder_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='username_id',
        ),
        migrations.AddField(
            model_name='users',
            name='username',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
