# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models
from shop.models.productmodel import Product
from django.utils.translation import ugettext_lazy as _

class CategoryManager(models.Manager):
    def root_categories(self):
        return self.filter(parent_category__isnull=True)


class Category(models.Model):
    '''
    This should be a node in a tree (mptt?) structure representing categories
    of products.
    Ideally, this should be usable as a tag cloud too (tags are just categories
    that are not in a tree structure). The display logic should be handle on a
    per-site basis
    '''

    class Meta(object):
        verbose_name = _("category")
        verbose_name_plural = _("categories")
        ordering = ['order']

    name = models.CharField(max_length=255)
    slug = models.SlugField()
    parent_category = models.ForeignKey('self',
                                        related_name="children",
                                        null=True, blank=True,
                                        verbose_name=_('Parent category'),
                                        )

    products = models.ManyToManyField(Product, related_name='categories',
                                      blank=True, null=True,
                                      verbose_name=_('Products'),
                                      )
    order = models.IntegerField(verbose_name=_('Ordering'), default=0)
    objects = CategoryManager()
    
    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', args=[self.slug])

    def get_products(self):
        '''
        Gets the products belonging to this category (not recursively)
        '''
        return self.products.all()

    def get_child_categories(self):
        return Category.objects.filter(parent_category=self)

