from django import forms
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django.forms import NumberInput, TextInput, Textarea
from django.db import models
from django.utils.html import format_html
from django_svg_image_form_field import SvgAndImageFormField

from .models import Category, Product, Brand

# Register your models here.

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = []
        field_classes = {
            'image': SvgAndImageFormField,
        }

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ['name']}
    form = CategoryForm


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ['name']}


class ProductAdmin(SummernoteModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':100})},
        models.IntegerField: {'widget': NumberInput(attrs={'size':100})},
        models.TextField: {'widget': Textarea(attrs={'rows': 30, 'cols': 100,})},
    }

    list_display = ('image_tag', 'name', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ['name']}
    summernote_fields = ('description', 'key_features', 'specification')

    def image_tag(self, obj):
        return format_html('<img style="width: 80px" src="{}" />'.format(obj.image.url))

    image_tag.short_description = 'Image'




admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
