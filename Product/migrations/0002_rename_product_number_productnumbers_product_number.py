# Generated by Django 4.0.4 on 2022-05-11 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productnumbers',
            old_name='Product_number',
            new_name='product_number',
        ),
    ]
