from django.contrib import admin
from .models import Reservation, Review, MenuItem, GalleryImage


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display  = ('name', 'email', 'phone', 'date', 'time', 'guests', 'created_at')
    list_filter   = ('date',)
    search_fields = ('name', 'email', 'phone')
    ordering      = ('-created_at',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display  = ('name', 'initials', 'likes', 'date_label', 'created_at')
    ordering      = ('-created_at',)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display   = ('name', 'tab', 'subcategory', 'badge', 'price', 'price2', 'sort_order', 'is_active')
    list_filter    = ('tab', 'subcategory', 'badge', 'is_active')
    search_fields  = ('name', 'description')
    list_editable  = ('sort_order', 'is_active', 'price', 'price2')
    ordering       = ('tab', 'subcategory', 'sort_order', 'name')

    def image_preview(self, obj):
        from django.utils.html import format_html
        if obj.image_url:
            return format_html('<img src="{}" style="height:60px;border-radius:6px;" />', obj.image_url)
        return '—'
    image_preview.short_description = 'Preview'

    fieldsets = (
        ('Item Info', {
            'fields': ('tab', 'subcategory', 'name', 'description', 'icon', 'badge', 'quote')
        }),
        ('Pricing', {
            'description': (
                'Spirits: price=30ml, price2=750ml | '
                'Wine: price=Glass, price2=Bottle | '
                'Pizza: price=Small, price2=Large | '
                'MO:MO: price=Steam, price2=Kothey, price3=Jhol, price4=Chilly | '
                'Everything else: price only'
            ),
            'fields': ('price', 'price2', 'price3', 'price4'),
        }),
        ('Display', {
            'fields': ('sort_order', 'is_active'),
        }),
    )


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display  = ('image_preview', 'title', 'category', 'is_large', 'sort_order', 'is_active')
    list_filter   = ('category', 'is_large', 'is_active')
    search_fields = ('title',)
    list_editable = ('sort_order', 'is_active', 'is_large')
    ordering      = ('sort_order', 'id')

    def image_preview(self, obj):
        from django.utils.html import format_html
        src = obj.src
        if src:
            return format_html('<img src="{}" style="height:60px;border-radius:6px;object-fit:cover;width:90px;" />', src)
        return '—'
    image_preview.short_description = 'Preview'

    fieldsets = (
        ('Image', {
            'fields': ('title', 'image', 'image_url', 'category'),
            'description': 'Upload a file from your desktop, or paste an external URL. Uploaded file takes priority.',
        }),
        ('Display', {
            'fields': ('is_large', 'sort_order', 'is_active'),
        }),
    )
