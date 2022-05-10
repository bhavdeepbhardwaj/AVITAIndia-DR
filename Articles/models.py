from django.db import models
from django.utils.text import gettext_lazy as _


# Create your models here.
# Banner Model
class Banner(models.Model):
    country = models.CharField(verbose_name=_("Country "), max_length=50, blank=True, null=True)
    thumbnail_path = models.ImageField(verbose_name=_("Web Image"), upload_to="media/images/Banner/web", default=None,
                                       blank=True, null=True)
    image_path = models.ImageField(verbose_name=_("Mob Image"), upload_to="media/images/Banner/mob", default=None,
                                   blank=True, null=True)
    status = models.CharField(verbose_name=_("Status"), max_length=8,
                              choices=[('Enable', 'Enable'), ('Disable', 'Disable')])
    seq = models.CharField(verbose_name=_("Seq "), max_length=50, blank=True, null=True)
    start_date = models.DateField(verbose_name=_("Start Date"), max_length=50, blank=True, null=True)
    end_date = models.DateField(verbose_name=_("End Date"), max_length=50, blank=True, null=True)
    url = models.CharField(verbose_name=_("Url"), max_length=50, blank=True, null=True)


# Blogs Model
class Blog(models.Model):
    country = models.CharField(verbose_name=_("Country "), max_length=50, blank=True, null=True)
    thumbnail_path = models.ImageField(verbose_name=_("Web Image"), upload_to="media/images/Banner/web", default=None,
                                       blank=True, null=True)
    image_path = models.ImageField(verbose_name=_("Mob Image"), upload_to="media/images/Banner/mob", default=None,
                                   blank=True, null=True)
    is_publish = models.CharField(verbose_name=_("Is Publish"), max_length=8,
                                  choices=[('Enable', 'Enable'), ('Disable', 'Disable')])
    publish_date = models.DateField(verbose_name=_("Publish Date"), max_length=50, blank=True, null=True)
    locale = models.CharField(verbose_name=_("Locale"), max_length=50, blank=True, null=True)
    title = models.CharField(verbose_name=_("Title"), max_length=50, blank=True, null=True)
    desc = models.TextField(verbose_name=_("Blog Description"), max_length=50)


# Event Model
class Event(models.Model):
    country = models.CharField(verbose_name=_("Country "), max_length=50, blank=True, null=True)
    thumbnail_path = models.ImageField(verbose_name=_("Web Image"), upload_to="media/images/Event/web", default=None,
                                       blank=True, null=True)
    image_path = models.ImageField(verbose_name=_("Mob Image"), upload_to="media/images/Event/mob", default=None,
                                   blank=True, null=True)
    is_publish = models.CharField(verbose_name=_("Is Publish"), max_length=8,
                                  choices=[('Enable', 'Enable'), ('Disable', 'Disable')])
    publish_date = models.DateField(verbose_name=_("Publish Date"), max_length=50, blank=True, null=True)
    locale = models.CharField(verbose_name=_("Locale"), max_length=50, blank=True, null=True)
    title = models.CharField(verbose_name=_("Title"), max_length=50, blank=True, null=True)
    desc = models.TextField(verbose_name=_("Blog Description"), max_length=50)


# News Model
class News(models.Model):
    country = models.CharField(verbose_name=_("Country "), max_length=50, blank=True, null=True)
    thumbnail_path = models.ImageField(verbose_name=_("Web Image"), upload_to="media/images/News/web", default=None,
                                       blank=True, null=True)
    image_path = models.ImageField(verbose_name=_("Mob Image"), upload_to="media/images/News/mob", default=None,
                                   blank=True, null=True)
    is_publish = models.CharField(verbose_name=_("Is Publish"), max_length=8,
                                  choices=[('Enable', 'Enable'), ('Disable', 'Disable')])
    publish_date = models.DateField(verbose_name=_("Publish Date"), max_length=50, blank=True, null=True)
    locale = models.CharField(verbose_name=_("Locale"), max_length=50, blank=True, null=True)
    title = models.CharField(verbose_name=_("Title"), max_length=50, blank=True, null=True)
    desc = models.TextField(verbose_name=_("Blog Description"), max_length=50)
