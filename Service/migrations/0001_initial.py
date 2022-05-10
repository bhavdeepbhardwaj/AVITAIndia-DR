# Generated by Django 4.0.4 on 2022-05-10 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceCenters',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('shop_Name', models.TextField(blank=True, max_length=50, null=True, verbose_name='Shop Name')),
                ('locale', models.TextField(blank=True, max_length=50, null=True, verbose_name='locale')),
                ('country', models.TextField(blank=True, max_length=50, null=True, verbose_name='country ')),
                ('address', models.TextField(blank=True, max_length=50, null=True, verbose_name='address')),
                ('opening_hour', models.DateTimeField(blank=True, null=True, verbose_name='opening_hour')),
                ('phone', models.TextField(blank=True, max_length=10, null=True, verbose_name='phone')),
                ('email', models.EmailField(blank=True, max_length=50, null=True, verbose_name='email')),
                ('city', models.TextField(blank=True, max_length=50, null=True, verbose_name='city')),
                ('state', models.TextField(blank=True, max_length=50, null=True, verbose_name='state')),
                ('pin', models.TextField(blank=True, max_length=50, null=True, verbose_name='pin')),
                ('latitude', models.FloatField(blank=True, max_length=50, null=True, verbose_name='latitude')),
                ('longitude', models.FloatField(blank=True, max_length=50, null=True, verbose_name='longitude')),
            ],
        ),
        migrations.CreateModel(
            name='WhereToBuys',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('shop_Name', models.TextField(blank=True, max_length=50, null=True, verbose_name='Shop Name')),
                ('locale', models.TextField(blank=True, max_length=50, null=True, verbose_name='locale')),
                ('country', models.TextField(blank=True, max_length=50, null=True, verbose_name='country ')),
                ('address', models.TextField(blank=True, max_length=50, null=True, verbose_name='address')),
                ('opening_hour', models.DateTimeField(blank=True, null=True, verbose_name='opening_hour')),
                ('phone', models.TextField(blank=True, max_length=10, null=True, verbose_name='phone')),
                ('email', models.EmailField(blank=True, max_length=50, null=True, verbose_name='email')),
                ('city', models.TextField(blank=True, max_length=50, null=True, verbose_name='city')),
                ('state', models.TextField(blank=True, max_length=50, null=True, verbose_name='state')),
                ('pin', models.TextField(blank=True, max_length=50, null=True, verbose_name='pin')),
                ('latitude', models.FloatField(blank=True, max_length=50, null=True, verbose_name='latitude')),
                ('longitude', models.FloatField(blank=True, max_length=50, null=True, verbose_name='longitude')),
            ],
        ),
    ]