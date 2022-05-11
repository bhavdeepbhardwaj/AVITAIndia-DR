from django.contrib import admin
from .models import ServiceCenter, WhereToBuy


class ServiceCentersAdmin(admin.ModelAdmin):
    list_display = (
        'shop_Name', 'locale', 'country', 'address', 'opening_hour', 'phone', 'email', 'city', 'state', 'pin',
        'latitude',
        'longitude')

    # Add filters for state and stars
    list_filter = ['shop_Name', 'pin']

    # Make the Business list searchable by name
    search_fields = ['shop_Name']

    # We don't want ids showing up
    exclude = ('id',)


admin.site.register(ServiceCenter, ServiceCentersAdmin)


class WhereToBuysAdmin(admin.ModelAdmin):
    list_display = (
        'shop_Name', 'locale', 'country', 'address', 'opening_hour', 'phone', 'email', 'city', 'state', 'pin',
        'latitude',
        'longitude')

    # Add filters for state and stars
    list_filter = ['shop_Name', 'pin']

    # Make the Business list searchable by name
    search_fields = ['shop_Name']

    # We don't want ids showing up
    exclude = ('id',)


admin.site.register(WhereToBuy, WhereToBuysAdmin)
