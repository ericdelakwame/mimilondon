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


class Product(models.Model):
    sub_category = models.ForeignKey(SubCategory, related_name='products', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, db_index=True)
    slug = models.CharField(max_length=50, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', null=True)
    image1 = models.ImageField(upload_to='products/%Y/%m/%d', null=True, blank=True)
    image2 = models.ImageField(upload_to='products/%Y/%m/%d', null=True, blank=True)
    image3 = models.ImageField(upload_to='products/%Y/%m/%d', null=True, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('shop:product_detail', kwargs={'product_id': self.pk})

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)


class Size(models.Model):
    product = models.ForeignKey(Product, related_name='sizes', on_delete=models.CASCADE, null=True)
    size = models.CharField(max_length=20, blank=True)
    class Meta:
        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'

    def __str__(self):
        return ' Size: {},'.format(self.size)


class Color(models.Model):
    product = models.ForeignKey(Product, related_name='colors', on_delete=models.CASCADE, null=True)
    color = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'

    def __str__(self):
        return ' Color: {},'.format(self.color)
