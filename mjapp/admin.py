from django.contrib import admin
from .models import *


# Register your models here.
class SericesAdmin(admin.ModelAdmin):
    list_display = ['name', 'amount', 'date']


admin.site.register(Services, SericesAdmin)


class PurchasesAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'amount', 'date']


admin.site.register(Purchases, PurchasesAdmin)



admin.site.register(ServiceOffered)


class BookingsAdmin(admin.ModelAdmin):
    list_display = ['name','date', 'status']


admin.site.register(Bookings, BookingsAdmin)
