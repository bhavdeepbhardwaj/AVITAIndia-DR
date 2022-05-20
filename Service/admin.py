from django.contrib import admin
from .models import ServiceCenter, WhereToBuy
from import_export.admin import ImportExportModelAdmin
from .resource import ServiceCenterResources, WhereToBuyResources


class ServiceCentersAdmin(ImportExportModelAdmin):
    resource_class = ServiceCenterResources
    list_display = ('shop_Name', 'locale', 'country', 'address', 'opening_hour', 'phone', 'email', 'city',
                    'state', 'pin', 'latitude', 'longitude')

    # Add filters for state and stars
    list_filter = ['shop_Name', 'pin']

    # Make the Business list searchable by name
    search_fields = ['shop_Name']

    # We don't want ids showing up
    exclude = ('id',)


admin.site.register(ServiceCenter, ServiceCentersAdmin)


# class WhereToBuysAdmin(admin.ModelAdmin):
class WhereToBuysAdmin(ImportExportModelAdmin):
    resource_class = WhereToBuyResources
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
