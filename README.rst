==============================
Django SHOP simple categories
==============================

This companion applicatoin to django SHOP provides an example of how shop implementors could implement a simple
category system.

It is perfectly usable as a simple category system.

In basic setup, you can select products on category admin page. If you want to set categories in product admin page,
subclass `ProductWithCategoryForm`, set `Meta` option `model` to your product model, and set this form as your product
form::

    from shop_simplecategories.admin import ProductWithCategoryForm

    class ProductForm(ProductWithCategoryForm):
        class Meta(object):
            model = Product

    class ProductAdmin(admin.ModelAdmin):
        form = ProductForm
