from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm
from webapp.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'index.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'detail.html'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'create.html'
    fields = ('name', 'category', 'description', 'image')
    success_url = reverse_lazy('webapp:index')


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'update.html'
    context_object_name = 'product'
    form_class = ProductForm

    def get_success_url(self):
        return reverse('webapp:product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
        model = Product
        template_name = 'delete.html'
        context_object_name = 'product'
        success_url = reverse_lazy('webapp:index')


