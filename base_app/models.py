from django.db import models
from uuid import uuid4
from os import path
from django.core.validators import RegexValidator


class CategoryDish(models.Model):
    name = models.CharField(unique=True, max_length=50, db_index=True)
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField(unique=True)

    def __str__(self):
        return f'{self.name}: {self.position}'

    class Meta:
        ordering = ('position', )


class Dish(models.Model):

    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/dishes', filename)

    name = models.CharField(max_length=50, unique=True)
    photo = models.ImageField(upload_to=get_file_name)
    dish_order = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)
    is_special = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    ingredients = models.CharField(max_length=100)
    desc = models.CharField(max_length=150, unique=True)
    category = models.ForeignKey(CategoryDish, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}: {self.price}'


class ModelFormRegistration(models.Model):
    mobile_regex = RegexValidator(regex=r'^(\d{3}[- .]?){2}\d{4}$', message='Phone in format xxx xxx xxxx')

    name = models.CharField(max_length=50, db_index=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15, validators=[mobile_regex])
    date = models.DateTimeField(auto_now_add=True)

    message = models.TextField(max_length=400, blank=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return f'{self.name}, {self.email}, {self.phone}'
