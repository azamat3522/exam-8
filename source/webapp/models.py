from django.contrib.auth.models import User
from django.db import models

# Create your models here.

CATEGORY_CHOICES = (
    ('other', 'Другое'),
    ('food', 'Еда'),
    ('clothes', 'Одежда'),
    ('household', 'Товары для дома'),
)

MARK_CHOICES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Товар')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES[0][0],
                                verbose_name='Категория')
    image = models.ImageField(upload_to='product_images', null=True, blank=True, verbose_name='Картинка')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', verbose_name='Автор')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews', verbose_name='Продукт')
    reviews_text = models.TextField(max_length=2000, verbose_name='Текст отзыва')
    mark = models.IntegerField(choices=MARK_CHOICES, verbose_name='Оценка')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.reviews_text

