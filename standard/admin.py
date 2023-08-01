from django.contrib import admin

from .models import *

# Register your models here.


admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)


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
