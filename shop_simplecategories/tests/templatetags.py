#-*- coding: utf-8 -*-
from decimal import Decimal
from django.test.testcases import TestCase

from classytags.tests import DummyParser, DummyTokens

from ..models import Category
from ..templatetags.shop_simplecategories_tags import RootCategoryTag


class RootCategoryTagTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name='Parent1')
        Category.objects.create(name='Parent2')
        Category.objects.create(name='Parent2', parent_category_id=1)
            
    def test01_should_only_return_parent_categories(self):
        tag = RootCategoryTag(DummyParser(), DummyTokens())
        result = tag.get_context({})
        self.assertTrue(result.has_key('categories'))
        self.assertEqual(len(result['categories']), 2)
