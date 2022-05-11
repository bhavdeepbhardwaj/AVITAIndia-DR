from django.contrib import admin
from .models import ProductType, ProductSerie, ProductModel, ProductNumber


class ProductTypeAdmin(admin.ModelAdmin):
    list_display = (
        'type_name',)

    # Add filters for state and stars
    list_filter = ['type_name']

    # Make the Business list searchable by name
    search_fields = ['type_name']

    # We don't want ids showing up
    exclude = ('id',)


admin.site.register(ProductType, ProductTypeAdmin)


class ProductSeriesAdmin(admin.ModelAdmin):
    list_display = ('product_type_id', 'series_name')

    # Add filters for state and stars
    list_filter = ['product_type_id', 'series_name']

    # Make the Business list searchable by name
    search_fields = ['series_name', 'product_type_id']

    # We don't want ids showing up
    exclude = ('id',)


admin.site.register(ProductSerie, ProductSeriesAdmin)


class ProductModelsAdmin(admin.ModelAdmin):
    list_display = ('product_series_id', 'models_number')

    # Add filters for state and stars
    list_filter = ['product_series_id', 'models_number']

    # Make the Business list searchable by name
    search_fields = ['models_number', 'product_series_id']

    # We don't want ids showing up
    exclude = ('id',)


admin.site.register(ProductModel, ProductModelsAdmin)


class ProductNumbersAdmin(admin.ModelAdmin):
    list_display = ('product_model_id', 'product_number', 'product_configuration')

    # Add filters for state and stars
    list_filter = ['product_model_id', 'product_number', 'product_configuration']

    # Make the Business list searchable by name
    search_fields = ['product_model_id', 'product_number']

    # We don't want ids showing up
    exclude = ('id',)


admin.site.register(ProductNumber, ProductNumbersAdmin)
