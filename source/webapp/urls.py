from django.urls import path

from webapp.views import ProductListView, ProductDetailView, ProductCreateView

app_name = 'webapp'

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),

]

