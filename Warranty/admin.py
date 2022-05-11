from django.contrib import admin
from .models import WarrantyExtend, WarrantyRegistration, Certificate


class WarrantyRegistrationAdmin(admin.ModelAdmin):
    list_display = (
        'user_id', 'product_number_id', 'serial_number', 'reseller_name', 'purchase_date', 'purchase_invoice',)

    # Add filters for state and stars
    list_filter = ['product_number_id', 'serial_number', 'reseller_name']

    # Make the Business list searchable by name
    search_fields = ['reseller_name', 'serial_number']

    # We don't want ids showing up
    exclude = ('id',)


admin.site.register(WarrantyRegistration, WarrantyRegistrationAdmin)


class WarrantyExtendAdmin(admin.ModelAdmin):
    list_display = (
        'user_id', 'product_number_id', 'serial_number', 'reseller_name', 'purchase_date', 'purchase_invoice')

    # Add filters for state and stars
    list_filter = ['product_number_id', 'serial_number', 'reseller_name']

    # Make the Business list searchable by name
    search_fields = ['reseller_name', 'serial_number']

    # We don't want ids showing up
    exclude = ('id',)


admin.site.register(WarrantyExtend, WarrantyExtendAdmin)


class CertificatesAdmin(admin.ModelAdmin):
    list_display = (
        'user_id', 'order_id', 'product_configuration', 'product_number', 'serial_number', 'reseller_name',
        'purchase_date', 'extend_date')

    # Add filters for state and stars
    list_filter = ['product_number', 'serial_number', 'reseller_name']

    # Make the Business list searchable by name
    search_fields = ['reseller_name', 'serial_number', 'order_id']

    # We don't want ids showing up
    exclude = ('id',)


admin.site.register(Certificate, CertificatesAdmin)
