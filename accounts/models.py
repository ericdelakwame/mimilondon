from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    tel_no = PhoneNumberField(blank=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    is_customer = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('accounts:user_detail', kwargs={'user_pk': self.pk})


class Customer(User):
    gender = models.CharField(
        max_length=20, choices=(
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('other', 'Other'),
        )
    )


    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('accounts:customer_detail', kwargs={'customer_pk': self.pk})


class Staff(User):
    pass

    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('accounts:staff_detail', kwargs={'staff_pk': self.pk})


class Admin(User):
    pass

    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('accounts:admin_detail', kwargs={'admin_pk': self.pk})
