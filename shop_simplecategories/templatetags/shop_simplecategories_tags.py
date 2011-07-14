from django import template

from classytags.helpers import InclusionTag

from ..models import Category

register = template.Library()


class RootCategoryTag(InclusionTag):
    template = 'shop_simplecategories/show_root_categories.html'
    name = 'show_root_categories'

    def get_context(self, context):
        return {'categories': Category.objects.root_categories(),}

register.tag(RootCategoryTag)
