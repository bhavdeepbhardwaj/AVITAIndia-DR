from django.db import models
from django.utils.text import gettext_lazy as _


# Create your models here.
# Product Type
class ProductType(models.Model):
    type_name = models.CharField(verbose_name=_("Type Name"), max_length=50, blank=True, null=True)

    def __str__(self):
        return self.type_name


# Product Series
class ProductSerie(models.Model):
    product_type_id = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    series_name = models.CharField(verbose_name=_("Product Series"), max_length=50, blank=True, null=True)

    def __str__(self):
        return self.series_name


# Product Models
class ProductModel(models.Model):
    product_series_id = models.ForeignKey(ProductSerie, on_delete=models.CASCADE)
    models_number = models.CharField(verbose_name=_("Product Model Number"), max_length=50, blank=True, null=True)

    def __str__(self):
        return self.models_number


# Product Numbers
class ProductNumber(models.Model):
    product_model_id = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    product_number = models.CharField(verbose_name=_("Product Number"), max_length=50, blank=True, null=True)
    product_configuration = models.CharField(verbose_name=_("Product Configuration"), max_length=50, blank=True,
                                             null=True)

    def __str__(self):
        return self.product_number
