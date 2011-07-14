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


For your convenience we have added a templatetag ``show_root_categories`` that 
outputs all root categories for you::

    {% load shop_simplecategories_tags %}

    <ul>{% show_root_categories %}</ul>

If you want to manipulate the output of that template tag, just override the template 
``shop_simplecategories/show_root_categories.html``
