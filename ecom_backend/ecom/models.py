from django.db import models

# Create your models here.

class Category(models.Model):

    class Meta:
        db_table = 'category'

    name = models.CharField('Categoria', max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.name

class Product(models.Model):

    class Meta:

        db_table = 'product'

    name = models.CharField('Nome', max_length=50, blank=False)
    description = models.TextField('Descrição', max_length=500, default='', blank=True)
    price = models.FloatField('Preço', default=0, blank=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

