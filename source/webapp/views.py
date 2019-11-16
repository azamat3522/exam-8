from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm, ReviewForm
from webapp.models import Product, Review


class ProductListView(ListView):
    model = Product
    template_name = 'product/index.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/detail.html'



class ProductCreateView(CreateView):
    model = Product
    template_name = 'product/create.html'
    fields = ('name', 'category', 'description', 'image')
    success_url = reverse_lazy('webapp:index')


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product/update.html'
    context_object_name = 'product'
    form_class = ProductForm

    def get_success_url(self):
        return reverse('webapp:product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
        model = Product
        template_name = 'product/delete.html'
        context_object_name = 'product'
        success_url = reverse_lazy('webapp:index')


class ReviewListView(ListView):
    model = Review
    template_name = 'product/index.html'


class ReviewCreateView(CreateView):
    model = Review
    template_name = 'review/create.html'
    form_class = ReviewForm


    def get_product(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Product, pk=pk)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.product = self.get_product()
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('webapp:product_detail', kwargs={'pk': self.object.product.pk})


class ReviewUpdateView(UpdateView):
    form_class = ReviewForm
    template_name = 'review/update.html'
    model = Review
    context_object_name = 'review'

    def get_success_url(self):
        return reverse('webapp:product_detail', kwargs={'pk': self.object.product.pk})


class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'review/delete.html'
    context_object_name = 'review'
    success_url = reverse_lazy('webapp:index')








