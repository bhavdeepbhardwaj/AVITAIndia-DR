from django.db import models
from django.utils.text import gettext_lazy as _


# Create your models here.
# Countries
class Countrie(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=50, blank=True, null=True)


# Campus
class Campu(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=50, blank=True, null=True)
    email = models.EmailField(verbose_name=_("Email"), max_length=50, blank=True, null=True)
    phone = models.CharField(verbose_name=_("Phone"), max_length=10, blank=True, null=True)
    internship = models.CharField(verbose_name=_("Internship"), max_length=8,
                                  choices=[('Yes', 'Yes'), ('No', 'No')])
    college = models.CharField(verbose_name=_("College"), max_length=50, blank=True, null=True)
    team = models.CharField(verbose_name=_("Team"), max_length=8,
                            choices=[('Yes', 'Yes'), ('No', 'No')])
    represent = models.CharField(verbose_name=_("Represent"), max_length=50, blank=True, null=True)


# Subscription
class Subscription(models.Model):
    email = models.EmailField(verbose_name=_("Email"), max_length=50, blank=True, null=True)
