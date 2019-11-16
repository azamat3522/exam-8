from django import forms

from webapp.models import Product, Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'image', 'description']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['author', 'product']