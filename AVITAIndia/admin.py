from django.contrib import admin
from .models import Countrie, Campu, Subscription


class CountriesAdmin(admin.ModelAdmin):
    list_display = (
        'name',)

    # Add filters for state and stars
    list_filter = ['name']

    # Make the Business list searchable by name
    search_fields = ['name']

    # We don't want ids showing up
    exclude = ('id',)


admin.site.register(Countrie, CountriesAdmin)


class CampusAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'internship', 'college', 'team', 'represent')

    # Add filters for state and stars
    list_filter = ['email']

    # Make the Business list searchable by name
    search_fields = ['email']

    # We don't want ids showing up
    exclude = ('id',)


admin.site.register(Campu, CampusAdmin)


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email',)

    # Add filters for state and stars
    list_filter = ['email']

    # Make the Business list searchable by name
    search_fields = ['email']

    # We don't want ids showing up
    exclude = ('id',)


admin.site.register(Subscription, SubscriptionAdmin)
