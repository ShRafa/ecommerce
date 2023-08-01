from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

@admin.register(Order)
class order_admin (admin.ModelAdmin):
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
    
