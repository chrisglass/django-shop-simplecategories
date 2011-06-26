#-*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from shop_simplecategories.models import Category
from django import forms
from django.utils.translation import ugettext_lazy as _

class ProductWithCategoryForm(forms.ModelForm):
  categories = forms.ModelMultipleChoiceField(
    queryset=Category.objects.all(),
    required=False,
    widget=FilteredSelectMultiple(
      verbose_name=_('categories'),
      is_stacked=False
    )
  )
  def __init__(self, *args, **kwargs):
    super(ProductWithCategoryForm, self).__init__(*args, **kwargs)

    if self.instance and self.instance.pk:
      self.fields['categories'].initial = self.instance.categories.all()

  def save(self, commit=True):
    product = super(ProductWithCategoryForm, self).save(commit=False)

    if commit:
      product.save()

    if product.pk:
      product.categories = self.cleaned_data['categories']
      self.save_m2m()

    return product


class CategoryAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("name",)}
  formfield_overrides = {
    models.ManyToManyField: {'widget': FilteredSelectMultiple(
      verbose_name=_('products'),
      is_stacked=False
      )},
  }
  list_display = ['name', 'slug', 'parent_category', 'order',]


admin.site.register(Category, CategoryAdmin)
