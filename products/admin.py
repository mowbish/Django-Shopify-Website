from django.contrib import admin

from products.models import Category, Product, Contact, IPaddress


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'slug')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_of_product', 'price', 'category', 'in_stock', 'is_active')
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ('is_active', 'in_stock')
    search_fields = ('name', 'description',)
    ordering = ('price',)
    list_editable = ['is_active', 'in_stock']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(IPaddress)
class IpAddressAdmin(admin.ModelAdmin):
    pass
