from django.contrib import admin

from .models import *


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "customer",
        "transaction_id",
        "complete",
        "date_orderd",
    ]
    list_filter = [
        "complete",
        "customer",
    ]
    search_fields = [
        "customer__name",
        "customer__email",
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "price",
        "image",
    ]

    search_fields = [
        "name",
    ]


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "email",
        "user",
    ]

    search_fields = [
        "name",
        "email",
        "user",
    ]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    search_fields = [
        "product__name",
    ]

    date_hierarchy = "date_added"


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = [
        "customer",
        "order",
        "address",
        "city",
        "state",
        "zipcode",
        "date_added",
    ]

    search_fields = [
        "customer__name",
        "address",
        "city",
        "state",
        "zipcode",
    ]

    list_filter = [
        "city",
        "state",
    ]

    date_hierarchy = "date_added"
