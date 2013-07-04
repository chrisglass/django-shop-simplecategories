==============================
Django SHOP simple categories
==============================

This companion application to django-SHOP provides an example of how shop
deployers could implement a simple category system.

It is perfectly usable as a simple category system.

In basic setup, you can select products on category admin page. If you want to
set categories in product admin page, subclass `ProductWithCategoryForm`, set
`Meta` option `model` to your product model, and set this form as your product
form::

    from shop_simplecategories.admin import ProductWithCategoryForm

    class ProductForm(ProductWithCategoryForm):
        class Meta(object):
            model = Product

    class ProductAdmin(admin.ModelAdmin):
        form = ProductForm


For your convenience we have added the templatetags ``show_root_categories`` and 
``show_root_with_child_categories`` for you. The first will outputs all root 
categories and the second one outputs all root categories with it's child (if present)::

    {% load shop_simplecategories_tags %}

    <ul>{% show_root_categories %}</ul>
	
or

    <ul>{% show_root_with_child_categories %}</ul>


If you want to manipulate the output of that template tag, just override the
templates ``shop_simplecategories/show_root_categories.html`` and/or  
``shop_simplecategories/show_root_with_child_categories.html`` .


Testing
========

If you want to run the testsuite make sure you have a virtual environment that
includes django and django-shop and run::

  cd shop_simplecategories/tests/
  ./runtests.py
