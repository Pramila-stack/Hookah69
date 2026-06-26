from django.contrib import admin
from .models import Reservation, Review, MenuItem


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date', 'time', 'guests', 'created_at')
    list_filter = ('date',)
    search_fields = ('name', 'email', 'phone')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'initials', 'likes', 'date_label', 'created_at')


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)
