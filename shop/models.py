from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=50, choices=(
        ('Men', 'Men'),
        ('Women', 'Women'),
        ('Children', 'Children'),
        ('Accessories', 'Accessories'),
        
    ))
    slug = models.SlugField(max_length=50, db_index=True, unique=True)

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:category_detail', kwargs={'category_pk': self.pk})


    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)



class SubCategory(models.Model):
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Sub Category'
        verbose_name_plural = 'Sub Categories'

    def __str__(self):
        return '{}: {}'.format(self.name, self.category.name)

    def get_absolute_url(self):
        return reverse('shop:subcategory_detail', kwargs={'subcategory_pk': self.pk})

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)
        super(SubCategory, self).save(*args, **kwargs)


class Size(models.Model):
    size = models.CharField(max_length=20, blank=True, unique=True)

    class Meta:
        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'

    def __str__(self):
        return '{}'.format(self.size)


class Color(models.Model):
    color = models.CharField(max_length=20, blank=True, unique=True)

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'

    def __str__(self):
        return '{}'.format(self.color)



class Product(models.Model):
    sub_category = models.ForeignKey(SubCategory, related_name='products', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/%Y/%m/%d', null=True)
    image1 = models.ImageField(upload_to='products/%Y/%m/%d', null=True, blank=True)
    image2 = models.ImageField(upload_to='products/%Y/%m/%d', null=True, blank=True)
    image3 = models.ImageField(upload_to='products/%Y/%m/%d', null=True, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    stock = models.PositiveIntegerField()
    sizes = models.ManyToManyField(Size, related_name='product_sizes')
    colors = models.ManyToManyField(Color, related_name='product_colors')
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('shop:product_detail', kwargs={'product_id': self.id})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)


class Options(models.Model):
    product = models.ForeignKey(Product, related_name='options', on_delete=models.CASCADE, null=True)
    size = models.CharField(max_length=20)
    color = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Product Option'
        verbose_name_plural = 'Product Options'

    def __str__(self):
        return '{} {} {}'.format(self.product.name, self.color, self.size)