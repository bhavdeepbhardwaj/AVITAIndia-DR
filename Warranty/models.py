from django.db import models
from django.utils.text import gettext_lazy as _


# Create your models here.
# Warranty Registration Model
class WarrantyRegistration(models.Model):
    user_id = models.CharField(verbose_name=_("User ID"), max_length=50, blank=True, null=True)
    product_number_id = models.CharField(verbose_name=_("Product Number"), max_length=50, blank=True, null=True)
    serial_number = models.CharField(verbose_name=_("Serial Number"), max_length=50, blank=True, null=True)
    reseller_name = models.CharField(verbose_name=_("Reseller Name"), max_length=50, blank=True, null=True)
    purchase_date = models.DateField(verbose_name=_("Purchase Date"), max_length=50, blank=True, null=True)
    purchase_invoice = models.FileField(verbose_name=_("Purchase Invoice"),
                                        upload_to="images/Warranty-Registration/purchase_invoice",
                                        max_length=5000, blank=True, null=True)


# Warranty Registration Model
class WarrantyExtend(models.Model):
    user_id = models.CharField(verbose_name=_("User ID"), max_length=50, blank=True, null=True)
    product_number_id = models.CharField(verbose_name=_("Product Number"), max_length=50, blank=True, null=True)
    serial_number = models.CharField(verbose_name=_("Serial Number"), max_length=50, blank=True, null=True)
    reseller_name = models.CharField(verbose_name=_("Reseller Name"), max_length=50, blank=True, null=True)
    purchase_date = models.DateField(verbose_name=_("Purchase Date"), max_length=50, blank=True, null=True)
    purchase_invoice = models.FileField(verbose_name=_("Purchase Invoice"),
                                        upload_to="images/Warranty-Extend/purchase_invoice",
                                        max_length=5000, blank=True, null=True)


# Warranty Registration Model
class Certificate(models.Model):
    user_id = models.CharField(verbose_name=_("User ID"), max_length=50, blank=True, null=True)
    order_id = models.CharField(verbose_name=_("Order ID"), max_length=50, blank=True, null=True)
    product_configuration = models.TextField(verbose_name=_("Product Configuration"), max_length=50, blank=True,
                                             null=True)
    product_number = models.CharField(verbose_name=_("Product Number"), max_length=50, blank=True, null=True)
    serial_number = models.CharField(verbose_name=_("Serial Number"), max_length=50, blank=True, null=True)
    reseller_name = models.CharField(verbose_name=_("Reseller Name"), max_length=50, blank=True, null=True)
    purchase_date = models.DateField(verbose_name=_("Purchase Date"), max_length=50, blank=True, null=True)
    extend_date = models.DateField(verbose_name=_("Extend Date"), max_length=50, blank=True, null=True)
