#-*- coding: utf-8 -*-
from decimal import Decimal
from django.test.testcases import TestCase
from shop.models.productmodel import Product
from shop_simplecategories.models import Category
from shop_simplecategories.views import CategoryDetailView


class CategoryDetailViewTestCase(TestCase):
    def create_fixtures(self):
        self.cat = Category()
        self.cat.name = 'Test Category'
        self.cat.save()
        
        self.product = Product()
        self.product.category = self.cat
        self.product.name = 'test'
        self.product.short_description = 'test'
        self.product.long_description = 'test'
        self.product.unit_price = Decimal('1.0')
        self.product.save()
    
    def test_01_get_context_works(self):
        self.create_fixtures()
        view = CategoryDetailView(kwargs={'pk':self.cat.id})
        setattr(view, 'object', view.get_object())
        ret = view.get_context_data()
        self.assertEqual(len(ret), 1)
        
    def test_02_get_context_works_with_list_of_products(self):
        self.create_fixtures()
        self.product.active = True
        self.product.save()
        view = CategoryDetailView(kwargs={'pk':self.cat.id})
        setattr(view, 'object', view.get_object())
        ret = view.get_context_data()
        self.assertEqual(len(ret), 2)