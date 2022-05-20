from django.db import models
from django.utils.text import gettext_lazy as _


# Create your models here.
# ServiceCenters
class ServiceCenter(models.Model):
    shop_Name = models.CharField(verbose_name=_("Shop Name"), max_length=100, blank=True, null=True)
    locale = models.CharField(verbose_name=_("Locale"), max_length=50, blank=True, null=True)
    country = models.CharField(verbose_name=_("Country "), max_length=100, blank=True, null=True)
    address = models.TextField(verbose_name=_("Address"), max_length=200, blank=True, null=True)
    opening_hour = models.CharField(verbose_name=_("opening_hour"), max_length=100,  blank=True, null=True)
    phone = models.CharField(verbose_name=_("Phone"), max_length=10, blank=True, null=True)
    email = models.EmailField(verbose_name=_("Email"), max_length=100, blank=True, null=True)
    city = models.CharField(verbose_name=_("City"), max_length=100, blank=True, null=True)
    state = models.CharField(verbose_name=_("State"), max_length=100, blank=True, null=True)
    pin = models.CharField(verbose_name=_("Pin"), max_length=50, blank=True, null=True)
    latitude = models.FloatField(verbose_name=_("Latitude"), max_length=50, blank=True, null=True)
    longitude = models.FloatField(verbose_name=_("Longitude"), max_length=50, blank=True, null=True)


# WhereToBuys
class WhereToBuy(models.Model):
    shop_Name = models.CharField(verbose_name=_("Shop Name"), max_length=100, blank=True, null=True)
    locale = models.CharField(verbose_name=_("Locale"), max_length=50, blank=True, null=True)
    country = models.CharField(verbose_name=_("Country "), max_length=100, blank=True, null=True)
    address = models.TextField(verbose_name=_("Address"), max_length=200, blank=True, null=True)
    opening_hour = models.CharField(verbose_name=_("opening_hour"), max_length=100,  blank=True, null=True)
    phone = models.CharField(verbose_name=_("Phone"), max_length=10, blank=True, null=True)
    email = models.EmailField(verbose_name=_("Email"), max_length=100, blank=True, null=True)
    city = models.CharField(verbose_name=_("City"), max_length=100, blank=True, null=True)
    state = models.CharField(verbose_name=_("State"), max_length=100, blank=True, null=True)
    pin = models.CharField(verbose_name=_("Pin"), max_length=50, blank=True, null=True)
    latitude = models.FloatField(verbose_name=_("Latitude"), max_length=50, blank=True, null=True)
    longitude = models.FloatField(verbose_name=_("Longitude"), max_length=50, blank=True, null=True)
