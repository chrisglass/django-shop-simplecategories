#-*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url
from shop.views import ShopListView
from shop_simplecategories.models import Category
from shop_simplecategories.views import CategoryDetailView


urlpatterns = patterns('',
    # Categories
    url(r'^$',
        ShopListView.as_view(model=Category),
        name='category_list'
        ),
    url(r'^/(?P<slug>[0-9A-Za-z-_.//]+)/$',
        CategoryDetailView.as_view(),
        name='category_detail'
        ),
)