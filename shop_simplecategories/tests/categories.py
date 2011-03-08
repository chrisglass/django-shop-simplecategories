#-*- coding: utf-8 -*-
from decimal import Decimal
from django.test.testcases import TestCase
from shop.models.productmodel import Product
from shop_simplecategories.models import Category


class CategoriesTestCase(TestCase):
    def create_fixtures(self):
        self.category = Category()
        self.category.name = "test_category"
        self.category.save()
        
        self.product = Product()
        self.product.name = 'test'
        self.product.short_description = 'test'
        self.product.long_description = 'test'
        self.product.unit_price = Decimal('1.0')
        self.product.category = self.category
        self.product.save()
        
    def test_01_category_unicode_returns_name(self):
        self.create_fixtures()
        ret = self.category.__unicode__()
        self.assertEqual(ret, self.category.name)
        
    def test_02_category_get_products_works(self):
        self.create_fixtures()
        ret = self.category.get_products()
        self.assertEqual(len(ret),1)
        cat_product = ret[0]
        self.assertEqual(cat_product,self.product)