from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    """
    Model for products
    """
    title = models.CharField(
        max_length=256,
        verbose_name='title'
    )
    price = models.PositiveSmallIntegerField(
        default=0, 
        validators=[MinValueValidator(0)],
        verbose_name='price'
    )
    description = models.TextField(
        verbose_name='description'
    )

    def __str__(self):
        return f'{self.id}'
    
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'Products'
