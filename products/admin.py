from django.contrib import admin

from products.models import ProductCategory, Product, Basket


admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'category']
    fields = ['name', 'description', 'category', ('price', 'quantity'), 'image']
    search_fields = ['name']
    ordering = ['name']


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ['product', 'quantity', 'creating_timestamp']
    readonly_fields = ['creating_timestamp']
    extra = 0