# Generated by Django 4.0.4 on 2022-05-11 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0004_alter_servicecenters_city_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WhereToBuys',
            new_name='ServiceCenter',
        ),
        migrations.RenameModel(
            old_name='ServiceCenters',
            new_name='WhereToBuy',
        ),
    ]
