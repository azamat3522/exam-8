from django.urls import path

from webapp.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    ReviewListView, ReviewCreateView, ReviewUpdateView, ReviewDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('review/', ReviewListView.as_view(), name='reviews'),
    path('review/add/product/<int:pk>/', ReviewCreateView.as_view(), name="review_add"),
    path('review/update/product/<int:pk>/', ReviewUpdateView.as_view(), name='review_update'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete')

]

