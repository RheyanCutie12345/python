from django.contrib import admin
from .models import User, UserPurchase, UserPurchaseHistory, Products


# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'Email', 'Name')
    search_fields = ('id', 'Email', 'Name')


class UserPurchaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'ProductName', 'Quantity', 'Total')
    search_fields = ('id', 'ProductName')


class UserPurchaseHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'ProductName', 'Quantity', 'Total', 'Status')
    search_fields = ('id', 'ProductName')


class ProductIdAdmin(admin.ModelAdmin):
    list_display = ('ProductId', 'ProductName', 'Price')
    search_fields = ('ProductId', 'ProductName')


admin.site.register(User, UserAdmin)
admin.site.register(UserPurchase, UserPurchaseAdmin)
admin.site.register(UserPurchaseHistory, UserPurchaseHistoryAdmin)
admin.site.register(Products, ProductIdAdmin)
