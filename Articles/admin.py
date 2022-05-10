from django.contrib import admin
from .models import Banner, Blog, Event, News


class BannerAdmin(admin.ModelAdmin):
    list_display = (
        'country', 'thumbnail_path', 'image_path', 'status', 'seq', 'start_date', 'end_date', 'url')

    # Add filters for state and stars
    list_filter = ['status']

    # Make the Business list searchable by name
    search_fields = ['seq']

    # We don't want ids showing up
    exclude = ('id',)


admin.site.register(Banner, BannerAdmin)


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'country', 'locale', 'title', 'desc', 'is_publish', 'thumbnail_path', 'image_path', 'publish_date')

    # Add filters for state and stars
    list_filter = ['title', 'is_publish']

    # Make the Business list searchable by name
    search_fields = ['title']

    # We don't want ids showing up
    exclude = ('id',)


admin.site.register(Blog, BlogAdmin)


class EventAdmin(admin.ModelAdmin):
    list_display = ('country', 'locale', 'title', 'desc', 'is_publish', 'thumbnail_path', 'image_path', 'publish_date')

    # Add filters for state and stars
    list_filter = ['title', 'is_publish']

    # Make the Business list searchable by name
    search_fields = ['title']

    # We don't want ids showing up
    exclude = ('id',)


admin.site.register(Event, EventAdmin)

class NewAdmin(admin.ModelAdmin):
    list_display = (
    'country', 'locale', 'title', 'desc', 'is_publish', 'thumbnail_path', 'image_path', 'publish_date')

    # Add filters for state and stars
    list_filter = ['title', 'is_publish']

    # Make the Business list searchable by name
    search_fields = ['title']

    # We don't want ids showing up
    exclude = ('id',)

admin.site.register(News, NewAdmin)