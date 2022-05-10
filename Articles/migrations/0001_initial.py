# Generated by Django 4.0.4 on 2022-05-10 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=50, null=True, verbose_name='Country ')),
                ('thumbnail_path', models.ImageField(blank=True, default=None, null=True, upload_to='media/images/Banner/web', verbose_name='Web Image')),
                ('image_path', models.ImageField(blank=True, default=None, null=True, upload_to='media/images/Banner/mob', verbose_name='Mob Image')),
                ('status', models.CharField(choices=[('Enable', 'Enable'), ('Disable', 'Disable')], max_length=8, verbose_name='Status')),
                ('seq', models.CharField(blank=True, max_length=50, null=True, verbose_name='Seq ')),
                ('start_date', models.DateField(blank=True, max_length=50, null=True, verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, max_length=50, null=True, verbose_name='End Date')),
                ('url', models.CharField(blank=True, max_length=50, null=True, verbose_name='Seq ')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=50, null=True, verbose_name='Country ')),
                ('thumbnail_path', models.ImageField(blank=True, default=None, null=True, upload_to='media/images/Banner/web', verbose_name='Web Image')),
                ('image_path', models.ImageField(blank=True, default=None, null=True, upload_to='media/images/Banner/mob', verbose_name='Mob Image')),
                ('is_publish', models.CharField(choices=[('Enable', 'Enable'), ('Disable', 'Disable')], max_length=8, verbose_name='Is Publish')),
                ('publish_date', models.DateField(blank=True, max_length=50, null=True, verbose_name='Publish Date')),
                ('locale', models.CharField(blank=True, max_length=50, null=True, verbose_name='Locale')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Title')),
                ('desc', models.TextField(max_length=50, verbose_name='Blog Description')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=50, null=True, verbose_name='Country ')),
                ('thumbnail_path', models.ImageField(blank=True, default=None, null=True, upload_to='media/images/Event/web', verbose_name='Web Image')),
                ('image_path', models.ImageField(blank=True, default=None, null=True, upload_to='media/images/Event/mob', verbose_name='Mob Image')),
                ('is_publish', models.CharField(choices=[('Enable', 'Enable'), ('Disable', 'Disable')], max_length=8, verbose_name='Is Publish')),
                ('publish_date', models.DateField(blank=True, max_length=50, null=True, verbose_name='Publish Date')),
                ('locale', models.CharField(blank=True, max_length=50, null=True, verbose_name='Locale')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Title')),
                ('desc', models.TextField(max_length=50, verbose_name='Blog Description')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=50, null=True, verbose_name='Country ')),
                ('thumbnail_path', models.ImageField(blank=True, default=None, null=True, upload_to='media/images/News/web', verbose_name='Web Image')),
                ('image_path', models.ImageField(blank=True, default=None, null=True, upload_to='media/images/News/mob', verbose_name='Mob Image')),
                ('is_publish', models.CharField(choices=[('Enable', 'Enable'), ('Disable', 'Disable')], max_length=8, verbose_name='Is Publish')),
                ('publish_date', models.DateField(blank=True, max_length=50, null=True, verbose_name='Publish Date')),
                ('locale', models.CharField(blank=True, max_length=50, null=True, verbose_name='Locale')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Title')),
                ('desc', models.TextField(max_length=50, verbose_name='Blog Description')),
            ],
        ),
    ]